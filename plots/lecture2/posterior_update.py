import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# ------------------------------------------------------
# Example: Bayesian update for log2 fold change of Gene X
# ------------------------------------------------------

# Define grid of possible log2 fold changes
effect = np.linspace(-3, 3, 400)

# PRIOR: before seeing data
# Assume most genes show no change (mean=0, wide uncertainty)
prior_mean = 0
prior_sd = 1.0
prior = norm.pdf(effect, loc=prior_mean, scale=prior_sd)

# LIKELIHOOD: data suggest upregulation (observed effect ~ +1)
# with standard error (measurement uncertainty) = 0.3
like_mean = 1.0
like_sd = 0.3
likelihood = norm.pdf(effect, loc=like_mean, scale=like_sd)

# POSTERIOR: combine prior and likelihood (since both Normal → analytical update)
post_var = 1 / (1/prior_sd**2 + 1/like_sd**2)
post_sd = np.sqrt(post_var)
post_mean = post_var * (prior_mean/prior_sd**2 + like_mean/like_sd**2)
posterior = norm.pdf(effect, loc=post_mean, scale=post_sd)

# ------------------------------------------------------
# Plot
# ------------------------------------------------------
plt.figure(figsize=(9, 6))
plt.plot(effect, prior, 'gray', lw=2, label='Prior (before data)')
plt.plot(effect, likelihood, 'skyblue', lw=2, label='Likelihood (data evidence)')
plt.plot(effect, posterior, 'crimson', lw=3, label='Posterior (updated belief)')

# Mark means
plt.axvline(prior_mean, color='gray', linestyle='--', alpha=0.6)
plt.axvline(like_mean, color='skyblue', linestyle='--', alpha=0.6)
plt.axvline(post_mean, color='crimson', linestyle='--', alpha=0.8)

plt.text(prior_mean - 0.3, max(prior)*0.9, 'Prior mean', color='gray')
plt.text(like_mean - 0.3, max(likelihood)*0.9, 'Data mean', color='skyblue')
plt.text(post_mean - 0.3, max(posterior)*0.9, 'Posterior mean', color='crimson')

plt.title('Bayesian Update: Gene X log₂ fold change')
plt.xlabel('log₂ fold change')
plt.ylabel('Probability density')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('posterior_update.png')

print(f"Posterior mean = {post_mean:.2f}, Posterior SD = {post_sd:.2f}")