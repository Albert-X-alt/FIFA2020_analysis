import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr

data = pd.read_excel('player.xlsx')
data = data[['skill_moves', 'wage_eur']].dropna()

wage_threshold = data['wage_eur'].quantile(0.99)
data = data[data['wage_eur'] <= wage_threshold]

var1, var2 = data['skill_moves'], data['wage_eur']

corr, p = spearmanr(var1, var2)

plt.figure(figsize=(10,6))
sns.regplot(
    x=var1, 
    y=np.log(var2+1),
    x_jitter=0.15,
    scatter_kws={'alpha':0.3, 'color':'#1f77b4'},
    line_kws={'color':'red', 'linewidth':2}
)

plt.title(f'Skill Moves vs Wage (Spearman r={corr:.2f}, p={p:.1e})')
plt.xlabel('Skill Moves (1-5 stars)')
plt.ylabel('Log(Weekly Wage + 1) (EUR)')
plt.xticks([1,2,3,4,5])
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
