import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# --- 1. Generate synthetic 2D data ---
X, y_true = make_blobs(n_samples=300, centers=3, cluster_std=1.2, random_state=42)

# --- 2. Apply K-Means ---
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_

# --- 3. Plotting ---
plt.figure(figsize=(8,6))
plt.scatter(X[:,0], X[:,1], c=y_kmeans, cmap='viridis', s=40, label='Data points')
plt.scatter(centroids[:,0], centroids[:,1], c='red', s=200, marker='X', label='Centroids')
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.savefig('k-means.png')
plt.close()