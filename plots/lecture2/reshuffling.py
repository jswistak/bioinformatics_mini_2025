import numpy as np

# Toy RNA-seq counts for one gene
control = np.array([45, 50, 41])
treatment = np.array([83, 79, 88])

# Observed difference in means
delta_obs = treatment.mean() - control.mean()

# Permutation test
data = np.concatenate([control, treatment])
labels = np.array([0]*3 + [1]*3)  # 0=control, 1=treatment

n_perm = 10000
deltas = np.zeros(n_perm)
for i in range(n_perm):
    perm_labels = np.random.permutation(labels)
    deltas[i] = data[perm_labels==1].mean() - data[perm_labels==0].mean()

# Empirical p-value (two-sided)
p_emp = (np.sum(np.abs(deltas) >= abs(delta_obs)) + 1) / (n_perm + 1)
print(f"Observed Δ = {delta_obs:.2f}, empirical p = {p_emp:.4f}")

import matplotlib.pyplot as plt
plt.hist(deltas, bins=30, alpha=0.7)
plt.axvline(delta_obs, color='red', linestyle='--', label='Observed')
plt.axvline(-delta_obs, color='red', linestyle='--')
plt.legend()
plt.xlabel('Δ (mean treatment - control)')
plt.ylabel('Permutation frequency')
plt.title('Empirical null distribution')
plt.savefig('reshuffling.png')