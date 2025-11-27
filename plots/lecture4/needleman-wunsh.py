import matplotlib.pyplot as plt
import numpy as np

# Example sequences
seq1 = "GAT"
seq2 = "GC"

# Example scoring matrix (filled manually for illustration)
matrix = np.array([
    [0, -1, -2],
    [-1, 1, 0],
    [-2, 0, 0]
])

fig, ax = plt.subplots(figsize=(5,5))
cax = ax.matshow(matrix, cmap='Blues')

# Add sequence labels
for j, s1 in enumerate("-"+seq1):
    ax.text(j, -0.5, s1, ha='center', va='bottom', fontsize=12)
for i, s2 in enumerate("-"+seq2):
    ax.text(-0.5, i, s2, ha='right', va='center', fontsize=12)

# Add matrix values
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        ax.text(j, i, str(matrix[i,j]), ha='center', va='center', color='black', fontsize=12)

# Highlight optimal path
optimal_path = [(2,2), (1,1), (0,0)]
for i,j in optimal_path:
    ax.add_patch(plt.Rectangle((j-0.5, i-0.5), 1, 1, fill=False, edgecolor='red', lw=2))

# Optional: add arrows showing traceback directions
arrows = [(0,0,1,1), (1,1,1,1), (2,2,0,-1)]  # Example arrows (customize)
# for y, x, dy, dx in arrows:
#     ax.arrow(x, y, dx*0.8, dy*0.8, head_width=0.1, head_length=0.1, fc='red', ec='red')

ax.set_xticks(range(matrix.shape[1]))
ax.set_yticks(range(matrix.shape[0]))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xlim(-1, matrix.shape[1])
ax.set_ylim(-1, matrix.shape[0])
plt.title("Needleman-Wunsch: Matrix & Optimal Path", pad=20)
plt.savefig('needleman-wunsh.png')
plt.close()