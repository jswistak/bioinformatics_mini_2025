import matplotlib.pyplot as plt
import numpy as np

bit_scores = np.linspace(50, 250, 100)
E_values = 1e-2 * np.exp(-0.03*bit_scores)  # example relationship

plt.figure(figsize=(6,4))
plt.plot(bit_scores, E_values, color='blue')
plt.yscale('log')
plt.xlabel('Bit Score')
plt.ylabel('E-value (log scale)')
plt.title('Relationship between Bit Score and E-value')
plt.axhline(1e-5, color='red', linestyle='--', label='Confident homology threshold')
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.savefig('e-value.png')
plt.close()