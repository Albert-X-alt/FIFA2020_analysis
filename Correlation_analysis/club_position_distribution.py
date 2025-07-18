import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kruskal, mannwhitneyu
from itertools import combinations

# Load and preprocess data
file_path = "player.xlsx"
df = pd.read_excel(file_path)

# Select relevant columns and drop missing values
data = df[['club_position', 'wage_eur']].dropna()

# Remove outliers with excessively high wages (top 1%)
wage_threshold = data['wage_eur'].quantile(0.99)
data = data[data['wage_eur'] <= wage_threshold]

# Statistical summary for each club position
print("="*40 + "\nDescriptive Statistics:\n" + "="*40)
stats = data.groupby('club_position')['wage_eur'].agg(['mean', 'median', 'std', 'count'])
print(stats)

# Visualization: Salary distribution in relation to club position
plt.figure(figsize=(12, 8))
sns.boxplot(x='club_position', y='wage_eur', data=data)
plt.title('Salary Distribution by Club Position')
plt.xlabel('Club Position')
plt.ylabel('Weekly Wage (EUR)')
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Statistical tests: Using Kruskal-Wallis H-test
print("\n" + "="*40 + "\nStatistical Tests:\n" + "="*40)
groups = [group['wage_eur'].values for name, group in data.groupby('club_position')]
if len(groups) >= 2:
    h_stat, p_value = kruskal(*groups)
    print(f"Kruskal-Wallis H-statistic: {h_stat:.3f}, p-value: {p_value:.4f}")

    if p_value < 0.05:
        print("\nPost-hoc Mann-Whitney U-tests with Bonferroni correction:")
        pairs = list(combinations(data['club_position'].unique(), 2))
        alpha = 0.05 / len(pairs)
        for pair in pairs:
            group1 = data[data['club_position'] == pair[0]]['wage_eur']
            group2 = data[data['club_position'] == pair[1]]['wage_eur']
            u_stat, p = mannwhitneyu(group1, group2, alternative='two-sided')
            print(f"{pair[0]} vs {pair[1]}: U = {u_stat}, p = {p:.4f}", 
                  "*" if p < alpha else "")
else:
    print("Insufficient groups for statistical comparison")