import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr

# Load and preprocess data
file_path = "player.xlsx"
df = pd.read_excel(file_path)

# Select the relevant columns and drop any rows with missing values
data = df[['age', 'wage_eur']].dropna()

# Remove wage outliers
wage_threshold = data['wage_eur'].quantile(0.99)  # Calculate the 99th percentile wage
data = data[data['wage_eur'] <= wage_threshold]  # Filter out wages above the threshold

# Calculate Spearman correlation
corr, p = spearmanr(data['age'], np.log(data['wage_eur'] + 1))  # Use log transformation for wage_eur

# Visualization
plt.figure(figsize=(10, 6))
sns.regplot(
    x=data['age'], 
    y=np.log(data['wage_eur'] + 1),
    x_jitter=0.15,
    scatter_kws={'alpha': 0.3, 'color': '#1f77b4'},
    line_kws={'color': 'red', 'linewidth': 2}
)

plt.title(f'Age vs Log(Wage) (Spearman r={corr:.2f}, p={p:.1e})')
plt.xlabel('Age')
plt.ylabel('Log(Wage + 1) (EUR)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
