import matplotlib.pyplot as plt

seq1 = "A-CGTAG"
seq2 = "ACCGT-G"

fig, ax = plt.subplots(figsize=(6,2))

for i, (a, b) in enumerate(zip(seq1, seq2)):
    color = 'green' if a==b else ('gray' if a=='-' or b=='-' else 'red')
    ax.text(i, 1, a, fontsize=16, ha='center', color=color)
    ax.text(i, 0, b, fontsize=16, ha='center', color=color)

ax.set_ylim(-0.5, 1.5)
ax.axis('off')
plt.title("Pairwise Sequence Alignment: gaps and mismatches")
plt.savefig('alignment_intro.png')