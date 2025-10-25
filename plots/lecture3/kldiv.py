import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# --- 1. Define two probability distributions ---
x = np.linspace(-5, 5, 500)

# Reference distribution P (standard normal)
P = norm.pdf(x, loc=0, scale=1)

# Approximating distribution Q (shifted and wider)
Q = norm.pdf(x, loc=1, scale=1.5)

# --- 2. Compute pointwise KL contribution ---
KL_pointwise = P * np.log(P / Q)

# --- 3. Plot distributions ---
plt.figure(figsize=(10,5))

plt.plot(x, P, label='P(x) - Reference', color='blue', lw=2)
plt.plot(x, Q, label='Q(x) - Approximation', color='red', lw=2)
plt.fill_between(x, 0, KL_pointwise, color='purple', alpha=0.3, label='KL Divergence Contribution')
plt.title("KL-Divergence Illustration")
plt.xlabel("x")
plt.ylabel("Probability / KL Contribution")
plt.legend()
plt.savefig('kldiv.png')
plt.close()

KL_total = np.sum(KL_pointwise) * (x[1] - x[0])
print(f"KL(P || Q) ≈ {KL_total:.4f}")