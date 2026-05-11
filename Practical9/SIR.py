#PSEUDOCODE
# BEGIN
#     Set total population N = 10000
#     Set infection rate beta = 0.3
#     Set recovery rate gamma = 0.05
#     Initialize S = 9999, I = 1, R = 0
#     Create lists to store S, I, R over time
#
#     FOR each time step from 1 to 1000
#         Calculate infection probability = beta * (I / N)
#         Randomly choose new infected from susceptible
#         Randomly choose new recovered from infected
#
#         Update S = S - new_infected
#         Update I = I + new_infected - new_recovered
#         Update R = R + new_recovered
#
#         Save current S, I, R to lists
#     END FOR
#
#     Plot S, I, R curves with labels and legend
# END

import numpy as np
import matplotlib.pyplot as plt

# Model parameters
N = 10000
beta = 0.3
gamma = 0.05

# Initial state
S = 9999
I = 1
R = 0

# Record history
S_list = [S]
I_list = [I]
R_list = [R]

total_time = 1000

# Simulation loop
for t in range(total_time):
    infection_prob = beta * (I / N)
    new_infected = np.random.binomial(S, infection_prob)
    new_recovered = np.random.binomial(I, gamma)
    
    # Update values
    S = S - new_infected
    I = I + new_infected - new_recovered
    R = R + new_recovered
    
    # Store results
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# Plot results
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label='Susceptible', color='blue')
plt.plot(I_list, label='Infected', color='red')
plt.plot(R_list, label='Recovered', color='green')

plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model')
plt.legend()
plt.show()