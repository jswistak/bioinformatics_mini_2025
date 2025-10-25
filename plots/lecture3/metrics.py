import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs

# --- 1. Generate synthetic 2D data ---
X, y_true = make_blobs(n_samples=30, centers=3, cluster_std=1.5, random_state=42)

# --- 2. Linkage matrices for different metrics ---
Z_euclidean = linkage(X, method='average', metric='euclidean')
Z_manhattan = linkage(X, method='average', metric='cityblock')
Z_correlation = linkage(X, method='average', metric='correlation')

# --- 3. Plot dendrograms side by side ---
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

dendrogram(Z_euclidean, ax=axes[0], color_threshold=15)
axes[0].set_title("Euclidean Distance")

dendrogram(Z_manhattan, ax=axes[1], color_threshold=15)
axes[1].set_title("Manhattan Distance")

dendrogram(Z_correlation, ax=axes[2], color_threshold=0.7)
axes[2].set_title("Correlation Distance")

for ax in axes:
    ax.set_xlabel("Sample Index")
    ax.set_ylabel("Distance")

plt.tight_layout()
plt.savefig('metrics.png')
plt.close()