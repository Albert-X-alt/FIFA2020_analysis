import pandas as pd
import torch
import torch.utils.data as data
import numpy as np
from sklearn.model_selection import train_test_split

mapping_5 = {
    76: 0, 75: 1, 74: 2, 72: 3, 71: 4, 70: 5, 69: 6, 68: 7, 67: 8, 66: 9,
    65: 10, 64: 11, 63: 12, 62: 13, 61: 14, 60: 15, 59: 16, 58: 17, 57: 18,
    56: 19, 55: 20, 54: 21, 53: 22, 52: 23, 51: 24, 50: 25, 49: 26, 48: 27,
    47: 28, 73: 29, 78: 30, 82: 31, 80: 32, 79: 33, 77: 34, 81: 35, 83: 36,
    84: 37, 85: 38, 86: 39, 90: 40, 87: 41, 89: 42, 88: 43, 91: 44, 92: 45,
    93: 46
}

mapping_6 = {
    87: 0, 75: 1, 74: 2, 72: 3, 78: 4, 82: 5, 85: 6, 71: 7, 84: 8, 70: 9,
    76: 10, 73: 11, 79: 12, 80: 13, 81: 14, 69: 15, 77: 16, 68: 17, 83: 18,
    67: 19, 66: 20, 65: 21, 64: 22, 63: 23, 62: 24, 61: 25, 60: 26, 59: 27,
    58: 28, 57: 29, 56: 30, 55: 31, 54: 32, 53: 33, 52: 34, 51: 35, 49: 36,
    86: 37, 50: 38, 88: 39, 90: 40, 89: 41, 91: 42, 93: 43, 92: 44, 95: 45
}

mapping_9 = {
    18: 0, 37: 1, 35: 2, 29: 3, 19: 4, 34: 5, 25: 6, 24: 7, 17: 8, 22: 9,
    31: 10, 30: 11, 28: 12, 36: 13, 27: 14, 26: 15, 21: 16, 23: 17, 33: 18,
    32: 19, 20: 20, 38: 21, 41: 22, 39: 23, 42: 24, 16: 25, 54: 26, 43: 27,
    40: 28
}
mapping_17 = {
    'ST': 0, 'GK': 1, 'SUB': 2, 'RCB': 3, 'CAM': 4, 'LCB': 5, 'RCM': 6, 'LB': 7,
    'RES': 8, 'RF': 9, 'RS': 10, 'LW': 11, 'LCM': 12, 'CDM': 13, 'RW': 14,
    'RB': 15, 'LM': 16, 'RDM': 17, 'RM': 18, 'LDM': 19, 'LS': 20, 'LWB': 21,
    'CB': 22, 'CM': 23, 'RWB': 24, 'LF': 25, 'LAM': 26, 'RAM': 27, 'CF': 28
}

mapping_28 = {
    4: 0, 3: 1, 2: 2, 5: 3, 1: 4
}
mapping_29 = {
    3: 0, 1: 1, 2: 2, 4: 3, 5: 4
}
mapping_30 = {
    1: 0, 2: 1, 3: 2, 4: 3, 5: 4
}

mapping_31 = {
    'High/Medium': 0, 'Medium/Medium': 1, 'Medium/High': 2, 'Medium/Low': 3,
    'High/Low': 4, 'Low/High': 5, 'Low/Low': 6, 'High/High': 7, 'Low/Medium': 8
}
mapping_32 = {
    'Normal (185+)': 0, 'Normal (170-185)': 1, 'Stocky (170-185)': 2,
    'Lean (185+)': 3, 'Lean (170-185)': 4, 'Stocky (170-)': 5, 'Normal (170-)': 6,
    'Lean (170-)': 7, 'Stocky (185+)': 8, 'Unique': 9
}

def z_score_normalize_tensor(data):
    normalized_data = (data - 2) / 2
    return normalized_data


class FIFA_dataset(data.Dataset):
    def __init__(self, dataframe):
        self.df = dataframe
        self.target_mean = self.df.iloc[:, 8].mean()
        self.target_std = self.df.iloc[:, 8].std()


        self.feature_mappings = {
            5: mapping_5,
            6: mapping_6,
            9: mapping_9,
            17: mapping_17,
            28: mapping_28,
            29: mapping_29,
            30: mapping_30,
            31: mapping_31,
            32: mapping_32
        }

    def __len__(self):
            return len(self.df)

    def __getitem__(self, index):
            columns_to_select = [5, 6, 9, 17, 28, 29, 30, 31, 32]

            features = self.df.iloc[index, columns_to_select].values
            target = self.df.iloc[index, 8]

            features = self._convert_to_numeric(features, columns_to_select)
            features = features.astype(np.float32)
            x = torch.tensor(features, dtype=torch.float32)

            y = torch.tensor(target, dtype=torch.float32).unsqueeze(0)
            y = (target - self.target_mean) / self.target_std
            y = torch.tensor(y, dtype=torch.float32).unsqueeze(0)
            return x,y

    def _convert_to_numeric(self, features, columns_to_select):
        converted_features = []
        for col_index, value in zip(columns_to_select, features):
            if isinstance(value, pd.Timestamp):
                converted_features.append(value.timestamp())
            elif isinstance(value, str):
                converted_features.append(self.feature_mappings[col_index].get(value, 0.0))
            elif pd.isnull(value):
                converted_features.append(0.0)
            else:
                converted_features.append(value)
        return np.array(converted_features)


if __name__ == '__main__':
    df = pd.read_excel('player.xlsx')

    dataset = FIFA_dataset(dataframe=df)

    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    train_dataset = FIFA_dataset(dataframe=train_df)
    test_dataset = FIFA_dataset(dataframe=test_df)

    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=False)


    for x, y in train_loader:
        print(f"Batch x shape: {x.shape}, Batch y shape: {y.shape}")
        break
    print(dataset.feature_mappings)
