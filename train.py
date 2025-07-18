import time
from sklearn.metrics import r2_score
import torch
import torch.nn as nn
import numpy as np
import torch.optim as optim
import pandas as pd
from FIFA22 import FIFA_dataset
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from model import simpleMLP


def train(model, train_loader, criterion, optimizer, device):
    model.train()
    model.to(device)
    with tqdm(train_loader, desc="Training", unit="batch") as t:
        for x, y in t:
            x, y = x.to(device), y.to(device)
            optimizer.zero_grad()
            outputs = model(x)
            loss = criterion(outputs, y)
            loss.backward()
            optimizer.step()
            t.set_postfix(loss=loss.item())

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
    val_loss/=len(val_loader)
    return val_loss
def evaluate_with_r2(model, test_loader, device):
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
    print(f'R² Score on the test set: {r2:.4f}')


if __name__== '__main__':
    df = pd.read_excel('player.xlsx')


    dataset = FIFA_dataset(dataframe=df)


    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)


    train_dataset = FIFA_dataset(dataframe=train_df)
    test_dataset = FIFA_dataset(dataframe=test_df)

    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=False)

    model = simpleMLP(9,1)

    criterion = nn.MSELoss()

    optimizer = optim.Adam(model.parameters(), lr=0.0001205)

    num_epochs = 200
    best_val_loss = float('inf')
    best_model_path = 'best_model2.pth'

    for epoch in range(num_epochs):
        train(model,train_loader,criterion,optimizer,'cuda')
        if((epoch+1)%5==0):
            loss = validate(model,test_loader,criterion,'cuda')
            print(f"print(f'Mean Squared Error of Epoch [{epoch + 1}/{num_epochs}], Val Loss: {loss:.4f}")
            if loss < best_val_loss:
                best_val_loss = loss
                torch.save(model.state_dict(), best_model_path)
                print(f"Saved model with validation loss: {loss:.4f}")
            evaluate_with_r2(model, test_loader, 'cuda')
            time.sleep(1)

    """print(f"std: {train_dataset.target_std}")
    print(f"mean: {train_dataset.target_mean}")"""
