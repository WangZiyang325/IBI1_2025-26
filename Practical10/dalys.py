# Practical 10 - Working with Global Health Data
# Analyzing DALYs (Disability Adjusted Life Years) across countries and time

import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Importing the dataset
# Use os.path to ensure the script works on any computer without manual path changes
current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, "dalys-rate-from-all-causes.csv")
dalys_data = pd.read_csv(path)

# 2. Show the 3rd and 4th columns (Year and DALYs) for the first 10 rows
# This provides an initial look at the data structure for Afghanistan
print("First 10 rows (Year and DALYs):")
first_10 = dalys_data.iloc[0:10, 2:4]
print(first_10)

# Finding the year with maximum DALYs in the first 10 rows (Afghanistan)
max_afghan_idx = first_10['DALYs'].idxmax()
max_afghan_year = first_10.loc[max_afghan_idx, 'Year']
print(f"In the first 10 years for Afghanistan, the maximum DALYs were recorded in: {max_afghan_year}")
# Comment: 1990 recorded the maximum DALYs in the first 10 recorded years for Afghanistan.

# 3. Use a Boolean to show all years for which DALYs were recorded in Zimbabwe
zimbabwe_data = dalys_data[dalys_data['Entity'] == "Zimbabwe"]
print("\nZimbabwe DALYs Data:")
print(zimbabwe_data[['Year', 'DALYs']])

# Comment: Zimbabwe data were recorded from 1990 to 2019 inclusive.
print(f"Zimbabwe data start year: {zimbabwe_data['Year'].min()}, end year: {zimbabwe_data['Year'].max()}")

# 4. Compute countries with maximum and minimum DALYs in 2019
data_2019 = dalys_data[dalys_data['Year'] == 2019]
max_2019_idx = data_2019['DALYs'].idxmax()
min_2019_idx = data_2019['DALYs'].idxmin()

max_country = data_2019.loc[max_2019_idx, 'Entity']
min_country = data_2019.loc[min_2019_idx, 'Entity']

# Comment: In 2019, the country with the maximum DALYs was Lesotho, and the minimum was Singapore.
print(f"\n2019 Maximum DALYs: {max_country}")
print(f"2019 Minimum DALYs: {min_country}")

# 5. Plot DALYs over time for a selected country (Singapore - Minimum DALYs in 2019)
plt.figure(figsize=(10, 6))
singapore_data = dalys_data[dalys_data['Entity'] == "Singapore"]
plt.plot(singapore_data['Year'], singapore_data['DALYs'], 'r-o', label='Singapore')

plt.title('DALYs Rate Over Time in Singapore (1990-2019)')
plt.xlabel('Year')
plt.ylabel('DALYs (Rate per 100,000)')
plt.grid(True)
plt.legend()
plt.savefig("singapore_dalys_trend.png")
plt.show()

# 6. Addressing the specific question (See question.txt for details)
# Question: How does the global average DALYs change from 1990 to 2019?
# This line addresses the question stated in question.txt
global_trend = dalys_data.groupby('Year')['DALYs'].mean()

plt.figure(figsize=(10, 6))
global_trend.plot(kind='line', marker='s', color='green')
plt.title('Global Average DALYs Trend (1990-2019)')
plt.xlabel('Year')
plt.ylabel('Mean DALYs Rate')
plt.grid(True)
plt.savefig("global_dalys_trend.png")
plt.show()