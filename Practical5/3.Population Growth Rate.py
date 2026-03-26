# This code calculates the percentage change in population for a list of countries between 2020 and 2024, sorts the countries by population growth rate, identifies the country with the highest and lowest growth rates, and visualizes the growth rates using a bar chart.
import matplotlib.pyplot as plt
# create a dictionary to store population data for each country in 2020 and 2024
population= {
    'UK':{'2020':66.7,'2024':69.2},
    'China':{'2020':1426,'2024':1410},
    'Italy':{'2020':59.4,'2024':58.9},
    'Brazil':{'2020':208.6,'2024':212.0},
    'USA':{'2020':331.6,'2024':340.1}
}

# calculate the percentage change in population for each country and store it in a new dictionary
change={}
for i in population:
    percentchange=round((population[i]['2024']-population[i]['2020'])/population[i]['2020']* 100, 2)
    print(i,'percent change:',percentchange,'%')
    change[i] = percentchange

# sort the countries by population growth rate in descending order and print the sorted list
sorted_change = sorted(change.items(), key=lambda x: x[1], reverse=True)
print("\nCountries sorted by population growth rate:")
for country, growth_rate in sorted_change:
    print(f"{country}: {growth_rate}%")

# identify the country with the highest and lowest population growth rates and print their names
max_growth_country = sorted_change[0][0]
min_growth_country = sorted_change[-1][0]
print(f"\nCountry with the highest population growth rate: {max_growth_country}")
print(f"Country with the lowest population growth rate: {min_growth_country}")

# create a bar chart to visualize the population growth rate change for each country
plt.bar( change.keys(), change.values() , color='orange')
plt.title("Population Growth Rate Change")
plt.xlabel("Countries")
plt.ylabel("Growth Rate (%)")
plt.axhline(y=0) # 0线
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()