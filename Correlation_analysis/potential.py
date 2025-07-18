import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, spearmanr
import numpy as np

# read
file_path = "player.xlsx"
df = pd.read_excel(file_path)

potential = df['potential']
wage = df['wage_eur']

# 检查数据是否符合正态分布
_, p_potential = shapiro(potential)
_, p_wage = shapiro(wage)

print(f"Potential normality p-value: {p_potential:.4f}")
print(f"Wage normality p-value: {p_wage:.4f}")

# 使用Spearman相关性分析
corr, p = spearmanr(potential, np.log(wage + 1))
print("\nUsing Spearman correlation:")
print(f"Correlation coefficient: {corr:.3f}")
print(f"P-value: {p:.4f}")

# 绘制对数变换后的数据散点图
plt.figure(figsize=(10, 6))
sns.regplot(x=potential, y=np.log(wage + 1), scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
plt.title(f'Spearman Correlation between Potential and Log(Wage)\n(r={corr:.2f}, p={p:.4f})')
plt.xlabel('Player Potential')
plt.ylabel('Log(Wage + 1) (EUR)')
plt.grid(True)  
plt.show()