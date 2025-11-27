import matplotlib.pyplot as plt
import numpy as np

# Example sequences
seq1 = "GACT"
seq2 = "GAAT"

# Example Smith-Waterman scoring matrix (manual for illustration)
matrix = np.array([
    [0,0,0,0,0],
    [0,2,0,0,0],
    [0,0,4,2,0],
    [0,0,2,3,1],
    [0,0,0,1,5]
])

fig, ax = plt.subplots(figsize=(5,5))
cax = ax.matshow(matrix, cmap='Greens')

# Sequence labels
for j, s1 in enumerate("-"+seq1):
    ax.text(j, -0.5, s1, ha='center', va='bottom', fontsize=12)
for i, s2 in enumerate("-"+seq2):
    ax.text(-0.5, i, s2, ha='right', va='center', fontsize=12)

# Matrix values
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        ax.text(j, i, str(matrix[i,j]), ha='center', va='center', color='black', fontsize=12)

# Highlight highest scoring cell
i,j = np.unravel_index(np.argmax(matrix), matrix.shape)
ax.add_patch(plt.Rectangle((j-0.5,i-0.5), 1, 1, fill=False, edgecolor='red', lw=2))

# Traceback path (example)
traceback_path = [(4,4),(3,3),(2,2)]
for y,x in traceback_path:
    ax.add_patch(plt.Rectangle((x-0.5, y-0.5), 1, 1, fill=False, edgecolor='blue', lw=2))

# Formatting
ax.set_xticks(range(matrix.shape[1]))
ax.set_yticks(range(matrix.shape[0]))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xlim(-1, matrix.shape[1])
ax.set_ylim(-1, matrix.shape[0])
plt.title("Smith–Waterman: Local Alignment Example & Optimal Path", pad=20)
plt.savefig('smith-waterman.png')
plt.close()