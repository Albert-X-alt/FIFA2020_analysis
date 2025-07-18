import optuna
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from sklearn.metrics import r2_score
from FIFA22 import FIFA_dataset
from model import simpleMLP
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

def train(model, train_loader, criterion, optimizer, device):
    model.train()
    model.to(device)

    for x, y in train_loader:
        x, y = x.to(device), y.to(device)
        optimizer.zero_grad()
        outputs = model(x)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()

def validate(model, val_loader, criterion, device):
    model.eval()
    model.to(device)
    val_loss = 0.0

    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            val_loss += loss.item()
    val_loss /= len(val_loader)
    return val_loss

def evaluate_with_r2(model, test_loader, test_dataset,device):
    model.eval()
    all_predictions = []
    all_targets = []

    with torch.no_grad():
        for x, y in test_loader:
            x, y = x.to(device), y.to(device)
            outputs = model(x)
            all_predictions.extend(outputs.cpu().numpy())
            all_targets.extend(y.cpu().numpy())

    all_predictions = np.array(all_predictions) * test_dataset.target_std + test_dataset.target_mean
    all_targets = np.array(all_targets) * test_dataset.target_std + test_dataset.target_mean

    r2 = r2_score(all_targets, all_predictions)
    return r2

def objective(trial):

    params = {
        "hidden_size0": trial.suggest_int("hidden_size0", 128, 2048),
        "hidden_size1": trial.suggest_int("hidden_size1", 128,2048),
        "hidden_size2": trial.suggest_int("hidden_size2", 128, 2048),
        "hidden_size3": trial.suggest_int("hidden_size3", 128, 2048),
        "hidden_size4": trial.suggest_int("hidden_size4", 128, 2048),
        "hidden_size5": trial.suggest_int("hidden_size5", 128, 2048),
        "learning_rate": trial.suggest_loguniform("learning_rate", 1e-4, 1e-3),

    }


    df = pd.read_excel('player.xlsx')
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
    train_dataset = FIFA_dataset(dataframe=train_df)
    test_dataset = FIFA_dataset(dataframe=test_df)
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)


    model = simpleMLP(9, 1)
    model.fc1 = nn.Linear(9, params["hidden_size0"])
    model.fc2 = nn.Linear(params["hidden_size0"], params["hidden_size1"])
    model.fc3 = nn.Linear(params["hidden_size1"], params["hidden_size2"])
    model.fc4 = nn.Linear(params["hidden_size2"], params["hidden_size3"])
    model.fc5 = nn.Linear(params["hidden_size3"], params["hidden_size4"])
    model.fc6 = nn.Linear(params["hidden_size4"], params["hidden_size5"])
    model.fc7 = nn.Linear(params["hidden_size5"], 1)




    #if params["optimizer_name"] == "Adam":
    optimizer = optim.Adam(model.parameters(), lr=params["learning_rate"])
    #elif params["optimizer_name"] == "SGD":
        #optimizer = optim.SGD(model.parameters(), lr=params["learning_rate"])
    #else:
        #raise NotImplementedError


    criterion = nn.MSELoss()


    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    for epoch in range(200):
        train(model, train_loader, criterion, optimizer, device)


    r2 = evaluate_with_r2(model, test_loader,test_dataset,device)

    return r2

if __name__ == "__main__":
    study = optuna.create_study(direction="maximize")
    study.optimize(objective, n_trials=10)

    print("Best trial:")
    trial = study.best_trial
    print(f"R² Score: {trial.value}")
    print("Best hyperparameters:", trial.params)