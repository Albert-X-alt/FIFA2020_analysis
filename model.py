import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np

class FIFAmodel(nn.Module):
    def __init__(self, input_size, output_size):
        super(FIFAmodel, self).__init__()
        self.fc1 = nn.Linear(input_size, 905)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(905, 1530)
        self.fc3 = nn.Linear(1530, 1068)
        self.fc4 = nn.Linear(1068, 451)
        self.fc5 = nn.Linear(451, 148)
        self.fc6 = nn.Linear(148, 587)
        self.fc7 = nn.Linear(587, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)

        x = self.fc2(x)
        x = self.relu(x)

        x = self.fc3(x)
        x = self.relu(x)

        x = self.fc4(x)
        x = self.relu(x)

        x = self.fc5(x)
        x = self.relu(x)

        x = self.fc6(x)
        x = self.relu(x)

        x = self.fc7(x)
        return x

def simpleMLP(input,output):
    return FIFAmodel(input,output)

print(simpleMLP(9,1))