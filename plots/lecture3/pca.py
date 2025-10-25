# --- PCA Example in 3D and 2D Projection ---
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import make_blobs
from mpl_toolkits.mplot3d import Axes3D  # for 3D plotting

# 1. Generate synthetic 3D dataset
X, y = make_blobs(n_samples=300, n_features=3, centers=3, cluster_std=1.2, random_state=42)

# 2. Perform PCA
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X)

# Explained variance
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Eigenvalues (variances):", pca.explained_variance_)

# 3. Plot original data in 3D
fig = plt.figure(figsize=(12, 5))

ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap='viridis', s=40)
ax.set_title("Original 3D Data")
ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.set_zlabel("Feature 3")

# 4. Plot PCA projection onto PC1 and PC2
ax2 = fig.add_subplot(1, 2, 2)
ax2.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', s=40)
ax2.set_title("Projection on PC1–PC2")
ax2.set_xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% var)")
ax2.set_ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% var)")

plt.tight_layout()
plt.savefig('pca.png')
plt.close()