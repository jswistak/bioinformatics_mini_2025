import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
np.random.seed(42)
m = 10000  # number of genes
prop_true_effects = 0.05  # 5% genes truly differentially expressed

# Simulate p-values
# True effects: smaller p-values
true_effects = np.random.beta(a=0.5, b=5, size=int(m * prop_true_effects))
# Null effects: uniformly distributed p-values
null_effects = np.random.uniform(0, 1, size=int(m * (1 - prop_true_effects)))
p_values = np.concatenate([true_effects, null_effects])
p_values.sort()

# Correction thresholds
alpha = 0.05
bonferroni_threshold = alpha / m
ranks = np.arange(1, m + 1)
bh_thresholds = (ranks / m) * alpha

# BH procedure: find largest p-value below its threshold
bh_cutoff_index = np.where(p_values <= bh_thresholds)[0]
bh_cutoff = p_values[bh_cutoff_index[-1]] if len(bh_cutoff_index) > 0 else None

# Plot
plt.figure(figsize=(10, 6))
plt.plot(ranks, p_values, '.', markersize=3, label='Observed p-values')
plt.plot(ranks, bh_thresholds, 'r--', label='BH FDR line (q=0.05)')
plt.axhline(y=alpha, color='gray', linestyle=':', label='Uncorrected α=0.05')
plt.axhline(y=bonferroni_threshold, color='purple', linestyle='-.', label='Bonferroni α/m')

# Highlight cutoff points
if bh_cutoff:
    plt.axhline(y=bh_cutoff, color='r', linestyle='-', alpha=0.5)
    plt.text(2000, bh_cutoff*1.2, f'BH cutoff ≈ {bh_cutoff:.4f}', color='r')

plt.xlabel('Ranked genes (sorted by p-value)')
plt.ylabel('p-value')
plt.title('Multiple Testing Correction in Gene Expression Analysis')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('benjamini-hochberg.png')