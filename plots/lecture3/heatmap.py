import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.preprocessing import StandardScaler

# --- 1. Generate synthetic gene expression data ---
# 20 genes (rows) x 10 samples (columns)
np.random.seed(42)
data = np.random.rand(20, 10) * 10

# Standardize genes (rows)
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# --- 2. Compute linkage for hierarchical clustering ---
# Cluster genes (rows)
Z_genes = linkage(data_scaled, method='ward')  # Ward linkage minimizes variance
# Optionally cluster samples (columns)
Z_samples = linkage(data_scaled.T, method='ward')

# --- 3. Create dendrogram + heatmap using seaborn clustermap ---
sns.set(font_scale=1)
g = sns.clustermap(
    data_scaled,
    row_linkage=Z_genes,
    col_linkage=Z_samples,
    cmap='vlag',            # Color map (red-blue)
    linewidths=0.5,
    figsize=(10,8)
)

plt.title("Hierarchical Clustering of Gene Expression")
plt.savefig('heatmap.png')
plt.close()