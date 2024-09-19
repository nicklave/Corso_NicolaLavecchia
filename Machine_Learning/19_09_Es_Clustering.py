import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, homogeneity_score


iris = load_iris()
X = iris.data
y = iris.target


kmeans = KMeans(n_clusters=3, random_state=42)
predizioni = kmeans.fit_predict(X)


pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)


ari = adjusted_rand_score(y, predizioni)
homogeneity = homogeneity_score(y, predizioni)

print(f'Adjusted Rand Index (ARI): {ari}')
print(f'Homogeneity Score: {homogeneity}')



plt.figure(figsize=(16, 6))

# Primo grafico: Cluster K-Means
plt.subplot(1, 2, 1)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=predizioni, cmap='viridis', marker='o', edgecolor='k', s=100)
plt.title('K-Means Clustering su Iris (PCA)')
plt.xlabel('Prima componente principale')
plt.ylabel('Seconda componente principale')
plt.colorbar(label='Cluster KMeans')

# Secondo grafico: Etichette Reali
plt.subplot(1, 2, 2)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', marker='o', edgecolor='k', s=100)
plt.title('Etichette Reali delle Specie di Iris (PCA)')
plt.xlabel('Prima componente principale')
plt.ylabel('Seconda componente principale')
plt.colorbar(label='Specie')


plt.tight_layout()
plt.show()



