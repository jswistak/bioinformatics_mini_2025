import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, SpectralClustering

# --- 1. Generate a non-convex dataset ---
X, y_true = make_moons(n_samples=200, noise=0.05, random_state=42)

# --- 2. Apply standard k-means (fails on non-convex data) ---
kmeans = KMeans(n_clusters=2, random_state=42)
y_kmeans = kmeans.fit_predict(X)

# --- 3. Apply spectral clustering ---
spectral = SpectralClustering(n_clusters=2, affinity='nearest_neighbors', n_neighbors=10, random_state=42)
y_spectral = spectral.fit_predict(X)

# --- 4. Plotting results ---
fig, axes = plt.subplots(1, 3, figsize=(18,5))

# Original data
axes[0].scatter(X[:,0], X[:,1], c=y_true, cmap='viridis', s=50)
axes[0].set_title("Original Data")
axes[0].set_xlabel("Feature 1")
axes[0].set_ylabel("Feature 2")

# K-means clustering
axes[1].scatter(X[:,0], X[:,1], c=y_kmeans, cmap='viridis', s=50)
axes[1].set_title("K-Means Clustering")
axes[1].set_xlabel("Feature 1")
axes[1].set_ylabel("Feature 2")

# Spectral clustering
axes[2].scatter(X[:,0], X[:,1], c=y_spectral, cmap='viridis', s=50)
axes[2].set_title("Spectral Clustering")
axes[2].set_xlabel("Feature 1")
axes[2].set_ylabel("Feature 2")

plt.tight_layout()
plt.savefig('spectral.png')
plt.close()