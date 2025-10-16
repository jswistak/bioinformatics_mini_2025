import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.neighbors import kneighbors_graph
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
from scipy.linalg import eigh

# --- 1. Generate non-convex data (two moons) ---
X, y_true = make_moons(n_samples=200, noise=0.05, random_state=42)

# --- 2. Build k-nearest neighbor similarity graph ---
n_neighbors = 10
A = kneighbors_graph(X, n_neighbors=n_neighbors, mode='connectivity', include_self=False)
A = 0.5 * (A + A.T)  # make symmetric

# --- 3. Compute graph Laplacian ---
D = np.diag(np.ravel(A.sum(axis=1)))
L = D - A

# --- 4. Compute first k eigenvectors of Laplacian ---
k = 2  # number of clusters
eigvals, eigvecs = eigh(L, D)  # generalized eigenvalue problem L v = λ D v
U = eigvecs[:, :k]
U = normalize(U)  # normalize rows

# --- 5. Cluster in spectral (eigenvector) space ---
y_spectral = KMeans(n_clusters=k, random_state=42).fit_predict(U)

# --- 6. Visualization ---
fig, axes = plt.subplots(1, 3, figsize=(18,5))

# (a) Original data with true structure
axes[0].scatter(X[:,0], X[:,1], c=y_true, cmap='viridis', s=50)
axes[0].set_title("Original Data (Two Moons)")
axes[0].set_xlabel("Feature 1")
axes[0].set_ylabel("Feature 2")

# (b) Similarity graph
for i in range(X.shape[0]):
    for j in range(X.shape[0]):
        if A[i, j] > 0:
            axes[1].plot([X[i,0], X[j,0]], [X[i,1], X[j,1]], color='lightgray', lw=0.5, alpha=0.5)
axes[1].scatter(X[:,0], X[:,1], c='black', s=10)
axes[1].set_title(f"{n_neighbors}-Nearest Neighbor Graph")
axes[1].set_xlabel("Feature 1")
axes[1].set_ylabel("Feature 2")

# (c) Spectral embedding and clustering
axes[2].scatter(U[:,0], U[:,1], c=y_spectral, cmap='viridis', s=50)
axes[2].set_title("Spectral Embedding (Eigenvector Space)")
axes[2].set_xlabel("1st Eigenvector")
axes[2].set_ylabel("2nd Eigenvector")

plt.tight_layout()
plt.savefig('lapacian.png')
plt.close()