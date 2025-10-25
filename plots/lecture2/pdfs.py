import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, uniform, expon, beta, binom, poisson, geom, nbinom

# -----------------------------
# Continuous distributions
# -----------------------------
x_cont = np.linspace(-3, 5, 500)
pdf_norm = norm.pdf(x_cont, loc=0, scale=1)
pdf_uniform = uniform.pdf(x_cont, loc=0, scale=4)  # range [0,4]
pdf_expon = expon.pdf(x_cont, scale=1)
pdf_beta = beta.pdf((x_cont + 1)/6, a=2, b=5)  # transform to [0,1] for Beta

# -----------------------------
# Discrete distributions
# -----------------------------
x_disc = np.arange(0, 15)
pmf_binom = binom.pmf(x_disc, n=10, p=0.5)
pmf_poisson = poisson.pmf(x_disc, mu=3)
pmf_geom = geom.pmf(x_disc, p=0.3)
pmf_nbinom = nbinom.pmf(x_disc, n=5, p=0.4)

# -----------------------------
# Plot
# -----------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: continuous
axes[0].plot(x_cont, pdf_norm, label='Normal(0,1)')
axes[0].plot(x_cont, pdf_uniform, label='Uniform(0,4)')
axes[0].plot(x_cont, pdf_expon, label='Exponential(λ=1)')
axes[0].plot(x_cont, pdf_beta, label='Beta(2,5) scaled')
axes[0].set_title('Continuous Distributions')
axes[0].set_xlabel('x')
axes[0].set_ylabel('PDF')
axes[0].legend()
axes[0].grid(alpha=0.3)

# Right panel: discrete
axes[1].stem(x_disc, pmf_binom, linefmt='C0-', markerfmt='C0o', basefmt='k', label='Binomial(n=10,p=0.5)')
axes[1].stem(x_disc, pmf_poisson, linefmt='C1-', markerfmt='C1s', basefmt='k', label='Poisson(λ=3)')
axes[1].stem(x_disc, pmf_geom, linefmt='C2-', markerfmt='C2^', basefmt='k', label='Geometric(p=0.3)')
axes[1].stem(x_disc, pmf_nbinom, linefmt='C3-', markerfmt='C3d', basefmt='k', label='NegBinom(r=5,p=0.4)')
axes[1].set_title('Discrete Distributions')
axes[1].set_xlabel('x')
axes[1].set_ylabel('PMF')
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('pdfs.png')