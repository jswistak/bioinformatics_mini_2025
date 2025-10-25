import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, SpectralClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score, adjusted_rand_score, normalized_mutual_info_score

# --- 1. Generate non-convex dataset (Two Moons) ---
X, y_true = make_moons(n_samples=300, noise=0.05, random_state=42)

# --- 2. Apply two clustering algorithms ---
kmeans = KMeans(n_clusters=2, random_state=42)
y_kmeans = kmeans.fit_predict(X)

spectral = SpectralClustering(n_clusters=2, affinity='nearest_neighbors', random_state=42)
y_spectral = spectral.fit_predict(X)

# --- 3. Compute metrics ---
def evaluate_clustering(X, y_pred, y_true):
    results = {}
    results['Silhouette'] = silhouette_score(X, y_pred)
    results['Davies-Bouldin'] = davies_bouldin_score(X, y_pred)
    results['ARI'] = adjusted_rand_score(y_true, y_pred)
    results['NMI'] = normalized_mutual_info_score(y_true, y_pred)
    return results

metrics_kmeans = evaluate_clustering(X, y_kmeans, y_true)
metrics_spectral = evaluate_clustering(X, y_spectral, y_true)

# --- 4. Visualization of clustering results ---
fig, axes = plt.subplots(1, 2, figsize=(12,5))

axes[0].scatter(X[:,0], X[:,1], c=y_kmeans, cmap='viridis', s=50)
axes[0].set_title("K-Means Clustering")

axes[1].scatter(X[:,0], X[:,1], c=y_spectral, cmap='viridis', s=50)
axes[1].set_title("Spectral Clustering")

for ax in axes:
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")

plt.tight_layout()
plt.savefig('cluster_validation.png')
plt.close()

# --- 5. Print metric comparison ---
import pandas as pd

results_df = pd.DataFrame([metrics_kmeans, metrics_spectral], 
                          index=['K-Means', 'Spectral Clustering']).T
print("\n🔍 Cluster Validation Metrics Comparison:\n")
print(results_df.round(3))