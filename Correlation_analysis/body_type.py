import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kruskal, mannwhitneyu
from itertools import combinations

df = pd.read_excel("player.xlsx")[['body_type', 'wage_eur']].dropna()

df['body_type_main'] = df['body_type'].str.split().str[0]
common_types = ['Normal', 'Stocky', 'Lean']
df['body_type_main'] = np.where(
    df['body_type_main'].isin(common_types),
    df['body_type_main'],
    'Unique'
)

print("="*40 + "\nDescriptive Statistics:\n" + "="*40)
stats = df.groupby('body_type_main')['wage_eur'].agg(['mean', 'median', 'std', 'count'])
print(stats)

plt.figure(figsize=(10, 6))
sns.boxplot(x='body_type_main', y='wage_eur', data=df)
plt.title('Salary Distribution by Body Type')
plt.show()

print("\n" + "="*40 + "\nStatistical Tests:\n" + "="*40)
groups = [group['wage_eur'].values for name, group in df.groupby('body_type_main')]
if len(groups) >= 2:
    h_stat, p_value = kruskal(*groups)
    print(f"Kruskal-Wallis H-statistic: {h_stat:.3f}, p-value: {p_value:.4f}")

    if p_value < 0.05:
        print("\nPost-hoc Mann-Whitney U Tests with Bonferroni correction:")
        pairs = list(combinations(df['body_type_main'].unique(), 2))
        alpha = 0.05 / len(pairs)
        for pair in pairs:
            group1 = df[df['body_type_main'] == pair[0]]['wage_eur']
            group2 = df[df['body_type_main'] == pair[1]]['wage_eur']
            u_stat, p = mannwhitneyu(group1, group2, alternative='two-sided')
            print(f"{pair[0]} vs {pair[1]}: U = {u_stat}, p = {p:.4f}", 
                  "*" if p < alpha else "")
else:
    print("Insufficient groups for statistical comparison")
