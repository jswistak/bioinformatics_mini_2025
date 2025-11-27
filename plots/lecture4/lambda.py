import numpy as np
from scipy.stats import gumbel_r
import matplotlib.pyplot as plt

# ------------------------------
# Step 1: Define scoring system
# ------------------------------
# Example: simple match/mismatch scores
match_score = 1
mismatch_score = -1
seq_length = 50

# ------------------------------
# Step 2: Simulate random alignments
# ------------------------------
n_simulations = 100000
scores = []

# Random sequences: letters A,C,G,T
letters = ['A','C','G','T']

for _ in range(n_simulations):
    seq1 = np.random.choice(letters, seq_length)
    seq2 = np.random.choice(letters, seq_length)
    
    # Compute raw alignment score
    score = sum(match_score if a==b else mismatch_score for a,b in zip(seq1, seq2))
    scores.append(score)

scores = np.array(scores)

# ------------------------------
# Step 3: Fit extreme value (Gumbel) distribution
# ------------------------------
params = gumbel_r.fit(scores)  # returns (loc=mu, scale=beta)
mu, beta = params
print(f"Fitted Gumbel parameters: mu={mu:.3f}, beta={beta:.3f}")

# ------------------------------
# Step 4: Estimate lambda and K (approximate)
# ------------------------------
# Lambda (scale parameter) is approximately 1/beta
lambda_est = 1 / beta
# K can be estimated from mu and beta as K = exp(-lambda*mu)
K_est = np.exp(-lambda_est * mu)
print(f"Estimated lambda: {lambda_est:.3f}")
print(f"Estimated K: {K_est:.3e}")

# ------------------------------
# Step 5: Plot histogram and fitted PDF
# ------------------------------
x = np.linspace(min(scores), max(scores), 500)
pdf = gumbel_r.pdf(x, loc=mu, scale=beta)

plt.figure(figsize=(10,5))
plt.hist(scores, bins=50, density=True, alpha=0.5, label='Simulated scores')
plt.plot(x, pdf, 'r-', lw=2, label='Fitted Gumbel PDF')
plt.xlabel('Alignment Score')
plt.ylabel('Probability Density')
plt.title('Simulation of Random Alignment Scores and Gumbel Fit')
plt.legend()
plt.savefig('lambda.png')
plt.close()
