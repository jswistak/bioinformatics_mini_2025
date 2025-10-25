import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

# Function to compute mean pairwise distance
def mean_pairwise_distance(points):
    dists = [np.linalg.norm(p1 - p2) for p1, p2 in combinations(points, 2)]
    return np.mean(dists)

# Number of points
n_points = 20
dimensions = [1, 2, 3, 10]
points_list = []
mean_distances = []

# Sample points and compute mean distances
for d in dimensions:
    points = np.random.rand(n_points, d)
    points_list.append(points)
    mean_distances.append(mean_pairwise_distance(points))

# Plotting in 2x2 grid
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

for i, ax in enumerate(axs.flat):
    d = dimensions[i]
    points = points_list[i]
    
    # Project to 2D for plotting
    if d == 1:
        ax.scatter(points[:,0], np.zeros(n_points), c='blue')
    else:
        ax.scatter(points[:,0], points[:,1], c='green' if d<=3 else 'red')
    
    ax.set_title(f'{d}D points\nMean distance ≈ {mean_distances[i]:.2f}')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])

plt.suptitle("Random Points in 1D, 2D, 3D, and 10D (projected to 2D)")
plt.savefig('dimension_static.png')
plt.close()

# Bar plot of mean distances
plt.bar(dimensions, mean_distances, color=['blue', 'green', 'orange', 'red'])
plt.xlabel("Dimension")
plt.ylabel("Mean pairwise distance")
plt.title("Mean pairwise distance increases with dimension")
plt.savefig('dimension_static_bar.png')
plt.close()