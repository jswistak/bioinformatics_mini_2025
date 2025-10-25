import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs

# --- 1. Generate synthetic data ---
X, y = make_blobs(n_samples=30, centers=3, cluster_std=1.0, random_state=42)

# --- 2. Compute linkage matrix ---
Z = linkage(X, method='ward')  # 'ward' minimizes variance within clusters

# --- 3. Plot dendrogram ---
plt.figure(figsize=(10,6))
dendrogram(Z, labels=np.arange(X.shape[0]), leaf_rotation=90, leaf_font_size=10, color_threshold=5)
plt.title("Agglomerative Hierarchical Clustering Dendrogram")
plt.xlabel("Sample Index")
plt.ylabel("Distance")
plt.savefig('dendrogram.png')
plt.close()