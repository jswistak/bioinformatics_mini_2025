import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.manifold import TSNE
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Generate synthetic 3D data ---
X, y = make_blobs(n_samples=300, n_features=3, centers=3, cluster_std=1.2, random_state=42)

# --- 2. Apply t-SNE to reduce to 2D ---
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_tsne = tsne.fit_transform(X)

# --- 3. Plot original 3D data ---
fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(1,2,1, projection='3d')
ax1.scatter(X[:,0], X[:,1], X[:,2], c=y, cmap='viridis', s=40)
ax1.set_title("Original 3D Data")
ax1.set_xlabel("Feature 1")
ax1.set_ylabel("Feature 2")
ax1.set_zlabel("Feature 3")

# --- 4. Plot 2D t-SNE projection ---
ax2 = fig.add_subplot(1,2,2)
ax2.scatter(X_tsne[:,0], X_tsne[:,1], c=y, cmap='viridis', s=40)
ax2.set_title("t-SNE 2D Projection")
ax2.set_xlabel("t-SNE 1")
ax2.set_ylabel("t-SNE 2")

plt.tight_layout()
plt.savefig('tsne.png')
plt.close()