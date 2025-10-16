import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import umap

# --- 1. Generate synthetic 3D data ---
X, y = make_blobs(n_samples=300, n_features=3, centers=3, cluster_std=1.2, random_state=42)

# --- 2. Apply UMAP to reduce to 2D ---
reducer = umap.UMAP(n_components=2, random_state=42)
X_umap = reducer.fit_transform(X)

# --- 3. Plot original 3D data ---
fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(1,2,1, projection='3d')
ax1.scatter(X[:,0], X[:,1], X[:,2], c=y, cmap='viridis', s=40)
ax1.set_title("Original 3D Data")
ax1.set_xlabel("Feature 1")
ax1.set_ylabel("Feature 2")
ax1.set_zlabel("Feature 3")

# --- 4. Plot 2D UMAP projection ---
ax2 = fig.add_subplot(1,2,2)
ax2.scatter(X_umap[:,0], X_umap[:,1], c=y, cmap='viridis', s=40)
ax2.set_title("UMAP 2D Projection")
ax2.set_xlabel("UMAP 1")
ax2.set_ylabel("UMAP 2")

plt.tight_layout()
plt.savefig('umap.png')
plt.close()