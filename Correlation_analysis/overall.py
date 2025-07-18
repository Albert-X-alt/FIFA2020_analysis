import pandas as pd
from scipy.stats import pearsonr, spearmanr, shapiro
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Specify the absolute path to the file
file_path = "player.xlsx"

# Check if the file exists
if not os.path.exists(file_path):
    print(f"File does not exist, please check the path: {file_path}")
else:
    # Load data
    data = pd.read_excel(file_path)

    # Extract relevant variables
    var1 = data['overall']
    var2 = data['wage_eur']

    # Normality test
    _, p1 = shapiro(var1.dropna()) 
    _, p2 = shapiro(var2.dropna())

    # Choose the correlation analysis method
    method = 'pearson' if (p1 > 0.05 and p2 > 0.05) else 'spearman'

    # Calculate the correlation
    if method == 'pearson':
        corr, p = pearsonr(var1, var2)
    else:
        corr, p = spearmanr(var1, var2)

    # Visualization
    sns.jointplot(x=var1, y=var2, kind='reg', height=7)
    plt.suptitle(f"{method.upper()} Correlation Analysis (r={corr:.2f}, p={p:.4f})")
    plt.xlabel('Overall Rating')
    plt.ylabel('Wage (EUR)')
    plt.show()

    # Output results
    print(f"Correlation method: {method}")
    print(f"Correlation coefficient: {corr:.2f}")
    print(f"P-value: {p:.4f}")