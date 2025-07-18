import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
file_path = "player.xlsx"
df = pd.read_excel(file_path)

# Select relevant columns and drop missing values
data = df[['club_position', 'wage_eur']].dropna()

# Remove outliers with excessively high wages (top 1%)
wage_threshold = data['wage_eur'].quantile(0.99)
data = data[data['wage_eur'] <= wage_threshold]

# Create a pivot table with club_position as rows and wage bins as columns
data['wage_eur_bin'] = pd.cut(data['wage_eur'], bins=np.logspace(np.log10(data['wage_eur'].min()), np.log10(data['wage_eur'].max()), num=10))
pivot_table = data.pivot_table(index='club_position', columns='wage_eur_bin', values='wage_eur', aggfunc='count', fill_value=0)

# Plot heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(pivot_table, annot=True, fmt="d", cmap='YlGnBu', cbar_kws={'label': 'Count'})
plt.title('Heatmap of Club Position vs Wage')
plt.xlabel('Wage EUR Bins')
plt.ylabel('Club Position')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()