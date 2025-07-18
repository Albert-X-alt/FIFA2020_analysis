import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr

# Load and preprocess data
df = pd.read_excel('player.xlsx')
data = df[['work_rate', 'wage_eur']].dropna()
data[['att_work', 'def_work']] = data['work_rate'].str.split('/', expand=True)

# Create ordered categorical variables
work_levels = ['Low', 'Medium', 'High']
data['att_work'] = pd.Categorical(data['att_work'], categories=work_levels, ordered=True)
data['def_work'] = pd.Categorical(data['def_work'], categories=work_levels, ordered=True)

# Remove wage outliers
wage_threshold = data['wage_eur'].quantile(0.99)
data = data[data['wage_eur'] <= wage_threshold]

# Create figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Common visualization settings
plot_kws = {
    'scatter_kws': {'alpha': 0.3, 'color': '#1f77b4'},
    'line_kws': {'color': 'red', 'linewidth': 2},
    'x_jitter': 0.15
}

# Plot 1: Attack Work Rate
att_corr, att_p = spearmanr(data['att_work'].cat.codes, np.log(data['wage_eur'] + 1))
sns.regplot(x=data['att_work'].cat.codes + 1, 
            y=np.log(data['wage_eur'] + 1), 
            ax=ax1,
            **plot_kws)
ax1.set_title(f'Attack Work Rate (ρ={att_corr:.2f}, p={att_p:.1e})', pad=15)
ax1.set_xlabel('Attack Work Rate Level', labelpad=10)
ax1.set_ylabel('Log(Wage + 1) (EUR)', labelpad=10)
ax1.set_xticks([1, 2, 3])
ax1.set_xticklabels(['Low', 'Medium', 'High'])

# Plot 2: Defense Work Rate
def_corr, def_p = spearmanr(data['def_work'].cat.codes, np.log(data['wage_eur'] + 1))
sns.regplot(x=data['def_work'].cat.codes + 1, 
            y=np.log(data['wage_eur'] + 1), 
            ax=ax2,
            **plot_kws)
ax2.set_title(f'Defense Work Rate (ρ={def_corr:.2f}, p={def_p:.1e})', pad=15)
ax2.set_xlabel('Defense Work Rate Level', labelpad=10)
ax2.set_xticks([1, 2, 3])
ax2.set_xticklabels(['Low', 'Medium', 'High'])

# Common formatting
for ax in [ax1, ax2]:
    ax.grid(alpha=0.3)
    ax.tick_params(axis='both', which='major', labelsize=10)
    ax.tick_params(axis='both', which='minor', labelsize=8)

plt.tight_layout()
plt.show()
