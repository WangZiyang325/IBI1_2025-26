# 2D Spatial SIR Model - Practical 9
# PSEUDOCODE
# Initialize grid, parameters, and random infection
# Create 2x2 subplot for visualization
# Loop over time steps:
#     Update infection spread to 8 neighbors
#     Update infected cells to recover
#     Plot grid at selected time steps
# Add main title and save the figure

import numpy as np
import matplotlib.pyplot as plt

# Set grid size and model parameters
size = 100
beta = 0.3
gamma = 0.05
total_steps = 100

# 0 = susceptible, 1 = infected, 2 = recovered
population = np.zeros((size, size), dtype=int)

# Random initial infection point
outbreak = np.random.choice(size, 2)
population[outbreak[0], outbreak[1]] = 1

# Function to get 8 surrounding neighbors of a cell
def get_neighbors(x, y):
    neighbors = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            if 0 <= x+dx < size and 0 <= y+dy < size:
                neighbors.append((x+dx, y+dy))
    return neighbors

# Create a 2x2 subplot layout to display multiple time steps
fig, axes = plt.subplots(2, 2, figsize=(8, 6))
axes = axes.flatten()  # Flatten the 2x2 array for easy indexing
plot_indices = [0, 10, 50, 90]  # Time steps to plot
current_plot = 0

# Main simulation loop
for t in range(total_steps):
    new_state = population.copy()
    infected_cells = np.where(population == 1)
    
    # Spread infection to neighboring cells
    for i in range(len(infected_cells[0])):
        x, y = infected_cells[0][i], infected_cells[1][i]
        neighbors = get_neighbors(x, y)
        for (nx, ny) in neighbors:
            if new_state[nx, ny] == 0 and np.random.rand() < beta:
                new_state[nx, ny] = 1
    
    # Handle recovery of infected cells
    infected_pos = np.where(new_state == 1)
    n_infected = len(infected_pos[0])
    recover_count = np.random.binomial(n_infected, gamma)
    if recover_count > 0:
        recover_indices = np.random.choice(n_infected, recover_count, replace=False)
        for idx in recover_indices:
            new_state[infected_pos[0][idx], infected_pos[1][idx]] = 2
    
    population = new_state
    
    # Plot results at specified time steps
    if t in plot_indices:
        ax = axes[current_plot]
        ax.imshow(population, cmap='viridis', interpolation='nearest')
        ax.set_title(f'Time = {t}')
        ax.set_xticks([0, 20, 40, 60, 80])
        ax.set_yticks([0, 20, 40, 60, 80])
        current_plot += 1

fig.suptitle('2D Spatial SIR Model', fontsize=18, y=0.98, weight='bold')

# Adjust layout and display the final plot
plt.tight_layout()
plt.show()