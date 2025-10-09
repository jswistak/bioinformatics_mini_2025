import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Simulate gene-level RNA-seq counts
# -----------------------------
np.random.seed(42)

n_genes = 100
mean_counts = np.linspace(5, 1000, n_genes)  # typical gene expression levels

# Negative Binomial variance: Var = mu + phi * mu^2
phi = 0.05  # dispersion parameter
true_variance = mean_counts + phi * mean_counts**2

# Add some random noise to simulate experimental variability
observed_variance = true_variance * np.random.normal(loc=1.0, scale=0.1, size=n_genes)

# -----------------------------
# Plot
# -----------------------------
plt.figure(figsize=(8,6))
plt.scatter(mean_counts, observed_variance, color='skyblue', edgecolor='black', alpha=0.8, label='Simulated genes')
plt.plot(mean_counts, true_variance, color='red', lw=2, label='Expected NB variance (Var=μ+φμ²)')

plt.xlabel('Mean counts per gene')
plt.ylabel('Variance of counts')
plt.title('Mean–Variance Relationship in RNA-seq (Negative Binomial)')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('rna-seq-nb.png')