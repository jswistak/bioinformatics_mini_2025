import numpy as np
import matplotlib.pyplot as plt

# --- 1. Simulate data with batch effect ---
np.random.seed(42)
n_samples = 50

# Batch 1
batch1 = np.random.randn(n_samples, 2) + np.array([0, 0])
# Batch 2 (shifted)
batch2 = np.random.randn(n_samples, 2) + np.array([5, 3])

# Combine batches
data = np.vstack([batch1, batch2])
batches = ['Batch1']*n_samples + ['Batch2']*n_samples

# --- 2. Simulate corrected data ---
# ComBat: aligns means (simple example)
combat = data.copy()
combat[50:] -= np.array([5, 3])

# Harmony: aligns clusters (shift + small random adjustment)
harmony = data.copy()
harmony[50:] -= np.array([4.5, 2.5]) + np.random.randn(n_samples, 2)*0.2

# Seurat integration: aligns clusters using anchors (shift + slight rotation)
theta = np.radians(15)
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
seurat = data.copy()
seurat[50:] = (seurat[50:] - np.array([4.5, 2.5])).dot(rotation_matrix)

# --- 3. Plotting ---
fig, axes = plt.subplots(1, 4, figsize=(20,5))

axes[0].scatter(data[:,0], data[:,1], c=['blue']*n_samples + ['red']*n_samples, alpha=0.7)
axes[0].set_title("Original Data (Batch Effect)")
axes[0].set_xlabel("PC1")
axes[0].set_ylabel("PC2")

axes[1].scatter(combat[:,0], combat[:,1], c=['blue']*n_samples + ['red']*n_samples, alpha=0.7)
axes[1].set_title("After ComBat")
axes[1].set_xlabel("PC1")

axes[2].scatter(harmony[:,0], harmony[:,1], c=['blue']*n_samples + ['red']*n_samples, alpha=0.7)
axes[2].set_title("After Harmony")
axes[2].set_xlabel("PC1")

axes[3].scatter(seurat[:,0], seurat[:,1], c=['blue']*n_samples + ['red']*n_samples, alpha=0.7)
axes[3].set_title("After Seurat Integration")
axes[3].set_xlabel("PC1")

plt.tight_layout()
plt.savefig('corrections.png')
plt.close()