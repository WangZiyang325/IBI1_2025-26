# SIR Model with Vaccination
# Practical 9 Modelling infections
import numpy as np
import matplotlib.pyplot as plt

# 1. Basic parameters (same as SIR.py)
N = 10000          # Total population
beta = 0.3          # Infection rate
gamma = 0.05        # Recovery rate
total_steps = 1000  # Total simulation time steps

# 2. Test vaccination rates: 0%, 10%, 20% ... 100%
vaccination_rates = np.arange(0, 1.01, 0.1)

# 3. Prepare figure for plotting
plt.figure(figsize=(6, 4), dpi=150)

# 4. Loop over every vaccination rate
for rate in vaccination_rates:
    
    # Special handling for 100% vaccination to avoid negative S
    if rate == 1.0:
        # 100% vaccinated: no one can be infected, I remains 0
        I_curve = [0] * (total_steps + 1)
        plt.plot(I_curve, label=f'{int(rate*100)}% vaccinated')
        continue

    # Calculate how many people are vaccinated
    vaccinated = int(N * rate)

    # Initial state of S, I, R
    S = N - vaccinated - 1  # susceptible = total - vaccinated - 1 infected
    I = 1                   # initial number of infected people
    R = 0                   # initial number of recovered people

    # List to store infected numbers over time
    I_curve = [I]

    # 5. Simulation loop (same logic as SIR.py)
    for step in range(total_steps):
        # Calculate infection probability
        infection_prob = beta * (I / N)
        
        # Randomly generate new infections
        new_infected = np.random.binomial(S, infection_prob)
        
        # Randomly generate new recoveries
        new_recovered = np.random.binomial(I, gamma)

        # Update S, I, R and keep values non-negative
        S = max(S - new_infected, 0)
        I = max(I + new_infected - new_recovered, 0)
        R = N - vaccinated - S - I

        # Record current number of infected people
        I_curve.append(I)

    # 6. Plot the infection curve for current vaccination rate
    plt.plot(I_curve, label=f'{int(rate*100)}% vaccinated')

# 7. Set figure labels, title and legend
plt.xlabel('Time')
plt.ylabel('Number of infected people')
plt.title('SIR model with different vaccination rates')
plt.legend(fontsize=7)
plt.savefig('sir_vaccination_curves.png', dpi=150, bbox_inches='tight')
plt.show()