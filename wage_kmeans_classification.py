import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
df = pd.read_excel('player.xlsx')
df = df.dropna(subset=['wage_eur'])
wages = df['wage_eur'].values.reshape(-1, 1)
scaler = StandardScaler()
wages_scaled = scaler.fit_transform(wages)
inertia = []
silhouette_scores = []
k_range = range(2, 11)  
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(wages_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(wages_scaled, kmeans.labels_))
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(k_range, inertia, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.subplot(1, 2, 2)
plt.plot(k_range, silhouette_scores, marker='o')
plt.title('Silhouette Score')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.tight_layout()
plt.show()
best_k = np.argmax(silhouette_scores) + 2  
print(f"Optimal number of clusters (k): {best_k}")
kmeans = KMeans(n_clusters=best_k, random_state=42)
clusters = kmeans.fit_predict(wages_scaled)
df['Cluster'] = clusters
for cluster in range(best_k):
    cluster_wages = df[df['Cluster'] == cluster]['wage_eur']
    min_wage = cluster_wages.min()
    max_wage = cluster_wages.max()
    print(f"Cluster {cluster}: Wage Range = {min_wage:.2f} EUR to {max_wage:.2f} EUR")
plt.figure(figsize=(10, 6))
for cluster in range(best_k):
    cluster_wages = df[df['Cluster'] == cluster]['wage_eur']
    plt.scatter(cluster_wages, np.zeros_like(cluster_wages), label=f'Cluster {cluster}')
plt.title('Wage Clusters (Optimal k)')
plt.xlabel('Wage (EUR)')
plt.legend()
plt.show()