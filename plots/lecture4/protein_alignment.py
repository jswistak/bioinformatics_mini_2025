import matplotlib.pyplot as plt

# Example sequences
seq1 = "MKTLLILALLAVALAGVQAAPQARQGKELKPLERLQKIEQLEQKQVEVIKDLTNVVSTGQIVLPEVQYQIKD"
seq2 = "MKTL---ILALLAVALAGVQAAPQ-SQGKELKPLDRLQKIEQLEQKQIEVIKDLTNVVSTGQIVLPEIQYQIKD"

# Example gap penalties illustration
penalties = ["High gap penalty", "Low gap penalty"]
alignments = [
    "MKTLLILALLAVALAGVQAAPQARQGKELKPLERLQKIEQLEQKQVEVIKDLTNVVSTGQIVLPEVQYQIKD\nMKTL---ILALLAVALAGVQAAPQ-SQGKELKPLDRLQKIEQLEQKQIEVIKDLTNVVSTGQIVLPEIQYQIKD",
    "MKTLLILALLAVALAGVQAAPQARQGKELKPLERLQKIEQLEQKQVEVIKDLTNVVSTGQIVLPEVQYQIKD\nMKTLILALLAVALAGVQAAPQ--SQGKELKPLDRLQKIEQLEQKQIEVIKDLTNVVSTGQIVLPEIQYQIKD"
]

fig, axes = plt.subplots(len(penalties), 1, figsize=(14, 4), constrained_layout=True)

for i, ax in enumerate(axes):
    ax.text(0.01, 0.5, alignments[i], fontfamily='monospace', fontsize=12, va='center')
    ax.set_title(penalties[i], fontsize=14, fontweight='bold')
    ax.axis('off')

# Annotate gap opening vs extension
for i, y in enumerate([0.85, 0.35]):
    axes[i].annotate("Gap opening", xy=(0.15, 0.6), xytext=(0.6, 0.8),
                     textcoords='axes fraction', arrowprops=dict(facecolor='red', shrink=0.05),
                     fontsize=12, color='red')
    axes[i].annotate("Gap extension", xy=(0.28, 0.6), xytext=(0.6, 0.7),
                     textcoords='axes fraction', arrowprops=dict(facecolor='blue', shrink=0.05),
                     fontsize=12, color='blue')

plt.suptitle("Effect of Gap Penalties on Protein Alignment", fontsize=16, fontweight='bold')
plt.savefig('protein_alignment.png')
plt.close()