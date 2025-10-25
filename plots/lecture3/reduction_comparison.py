import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap

# --- 1. Generate synthetic 3D data ---
X, y = make_blobs(n_samples=300, n_features=3, centers=3, cluster_std=1.2, random_state=42)

# --- 2. PCA ---
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# --- 3. t-SNE ---
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_tsne = tsne.fit_transform(X)

# --- 4. UMAP ---
reducer = umap.UMAP(n_components=2, random_state=42)
X_umap = reducer.fit_transform(X)

# --- 5. Plotting ---
fig, axes = plt.subplots(1, 3, figsize=(18,5))

# PCA plot
axes[0].scatter(X_pca[:,0], X_pca[:,1], c=y, cmap='viridis', s=40)
axes[0].set_title("PCA Projection")
axes[0].set_xlabel("PC1")
axes[0].set_ylabel("PC2")

# t-SNE plot
axes[1].scatter(X_tsne[:,0], X_tsne[:,1], c=y, cmap='viridis', s=40)
axes[1].set_title("t-SNE Projection")
axes[1].set_xlabel("t-SNE 1")
axes[1].set_ylabel("t-SNE 2")

# UMAP plot
axes[2].scatter(X_umap[:,0], X_umap[:,1], c=y, cmap='viridis', s=40)
axes[2].set_title("UMAP Projection")
axes[2].set_xlabel("UMAP 1")
axes[2].set_ylabel("UMAP 2")

plt.tight_layout()
plt.savefig('reduction_comparison.png')
plt.close()