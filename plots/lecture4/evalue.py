import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gumbel_r

# Parameters for Gumbel distribution (example values)
mu = 50    # location parameter
beta = 10  # scale parameter

# Raw scores
S = np.linspace(0, 120, 500)

# Probability density function (PDF) of Gumbel
pdf = gumbel_r.pdf(S, loc=mu, scale=beta)

# Compute E-value (expected number of hits above score S)
# Here we assume a database size factor (m*n*K) = 1e6 for illustration
K_mn = 1e6
E_value = K_mn * (1 - gumbel_r.cdf(S, loc=mu, scale=beta))

# Plot
plt.figure(figsize=(10,5))
plt.plot(S, pdf, label='Score Distribution (Gumbel PDF)')
plt.twinx()  # secondary axis for E-value
plt.plot(S, E_value, 'r--', label='E-value', linewidth=2)
plt.yscale('log')
plt.xlabel('Alignment Raw Score (S)')
plt.ylabel('PDF / E-value (log scale)')
plt.title('E-value vs Alignment Score')
plt.legend(loc='upper right')
plt.grid(True)
plt.savefig('evalue.png')
plt.close()