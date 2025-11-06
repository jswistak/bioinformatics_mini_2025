import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Example PAM250 snippet
data = {
    'A': [2, -2, 0, -1],
    'R': [-2, 6, 0, -1],
    'N': [0, 0, 2, 2],
    'D': [-1, -1, 2, 4]
}
aa_labels = ['A','R','N','D']
df = pd.DataFrame(data, index=aa_labels)

plt.figure(figsize=(4,3))
sns.heatmap(df, annot=True, cmap='RdYlGn_r', center=0, cbar_kws={'label':'Score'})
plt.title("PAM250 Matrix Snippet")
plt.savefig('pam.png')
plt.close()