import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6,4))

# Draw ancestor
ax.plot([0, 1], [2, 2], 'k-', lw=2)  # ancestor branch
ax.text(-0.1, 2, "Ancestor", fontsize=10, va='center')

# Duplication
ax.plot([1, 2], [2, 3], 'b-', lw=2)  # Paralog 1
ax.plot([1, 2], [2, 1], 'b-', lw=2)  # Paralog 2
ax.text(2.1, 3, "Paralog 1", fontsize=10, va='center', color='blue')
ax.text(2.1, 1, "Paralog 2", fontsize=10, va='center', color='blue')

# Speciation
ax.plot([2, 3], [3, 3.5], 'g-', lw=2)  # Ortholog A
ax.plot([2, 3], [1, 0.5], 'g-', lw=2)  # Ortholog B
ax.text(3.1, 3.5, "Ortholog A", fontsize=10, va='center', color='green')
ax.text(3.1, 0.5, "Ortholog B", fontsize=10, va='center', color='green')

# Formatting
ax.set_ylim(0, 4)
ax.set_xlim(-0.5, 3.5)
ax.axis('off')
plt.title("Gene Duplication and Speciation: Orthologs vs Paralogs")
plt.show()