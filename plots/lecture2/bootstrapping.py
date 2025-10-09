import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Original gene counts
# -----------------------------
counts = np.array([50, 52, 48, 55, 60, 53])
original_mean = np.mean(counts)

# -----------------------------
# Bootstrap
# -----------------------------
n_bootstrap = 1000
bootstrap_means = []

np.random.seed(42)  # for reproducibility

for _ in range(n_bootstrap):
    sample = np.random.choice(counts, size=len(counts), replace=True)
    bootstrap_means.append(np.mean(sample))

bootstrap_means = np.array(bootstrap_means)

# -----------------------------
# 95% Confidence Interval
# -----------------------------
ci_lower = np.percentile(bootstrap_means, 2.5)
ci_upper = np.percentile(bootstrap_means, 97.5)

# -----------------------------
# Plot
# -----------------------------
plt.figure(figsize=(9,6))
plt.hist(bootstrap_means, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(original_mean, color='red', linestyle='-', linewidth=2, label=f'Original mean = {original_mean:.2f}')
plt.axvline(ci_lower, color='green', linestyle='--', linewidth=2, label=f'95% CI lower = {ci_lower:.2f}')
plt.axvline(ci_upper, color='green', linestyle='--', linewidth=2, label=f'95% CI upper = {ci_upper:.2f}')
plt.title('Bootstrap Distribution of Gene X Mean (n=6 counts, 1000 resamples)')
plt.xlabel('Bootstrapped Mean')
plt.ylabel('Frequency')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('bootstrap_distribution.png')

print(f"Bootstrap 95% CI: [{ci_lower:.2f}, {ci_upper:.2f}]")