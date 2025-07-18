import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Specify the absolute path to the Excel file
file_path = "player.xlsx"

# Load the data from the Excel file
data = pd.read_excel(file_path)

# Remove outliers in wage data
wage_threshold = data['wage_eur'].quantile(0.99)
data = data[data['wage_eur'] <= wage_threshold]

# Create age groups
bins = [15, 20, 25, 30, 35, 40, 45, 50]
labels = ['15-20', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50']
data['age_group'] = pd.cut(data['age'], bins=bins, labels=labels, right=False)

# Plot a violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='age_group', y='wage_eur', data=data, inner=None, color=".8")
sns.stripplot(x='age_group', y='wage_eur', data=data, jitter=True, size=4, color=".2", linewidth=0)

# Add title and labels
plt.title('Salary Distribution by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Wage (EUR)')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent clipping of labels
plt.tight_layout()

# Display the plot
plt.show()