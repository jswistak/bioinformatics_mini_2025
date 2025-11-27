import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Example BLOSUM62 snippet
data = {
    'A': [4, -1, -2, -2],
    'R': [-1, 5, 0, -2],
    'N': [-2, 0, 6, 1],
    'D': [-2, -2, 1, 6]
}
aa_labels = ['A','R','N','D']
df = pd.DataFrame(data, index=aa_labels)

plt.figure(figsize=(4,3))
sns.heatmap(df, annot=True, cmap='RdYlGn_r', center=0, cbar_kws={'label':'Score'})
plt.title("BLOSUM62 Matrix Snippet")
plt.savefig('blosum.png')