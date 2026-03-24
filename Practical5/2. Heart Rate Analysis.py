import numpy as np
import matplotlib.pyplot as plt

# create a dataset of resting heart rates for a group of patients
heart_rates = (72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64)

# calculate the number of patients and the mean resting heart rate
num_patients = len(heart_rates)
mean_hr = round(np.mean(heart_rates))
print("The dataset contains",num_patients,'patients, and the mean resting heart rate is', mean_hr,' bpm.')

# categorize the heart rates into low, normal, and high categories
low=[]
normal=[]
high=[]
for i in heart_rates:
    if i < 60:
        low.append(i)
    elif 60 <=  i <= 120:
        normal.append(i)
    else:
        high.append(i)
a = len(low)
b = len(normal)
c = len(high)
print('Number of patients with low heart rate:', a)
print('Number of patients with normal heart rate:', b)
print('Number of patients with high heart rate:', c)
# determine which category has the largest number of patients
maxcount = max({'low': a, 'normal': b, 'high': c})
print('The category with the largest number of patients is:', maxcount)

# create a pie chart to visualize the distribution of heart rate categories
labels = ['Low (<60 bpm)', 'Normal (60-120 bpm)', 'High (>120 bpm)']
colors = ['lightcoral', 'lightgreen', 'lightskyblue']
sizes = [a, b, c]
explode = (0.1, 0, 0)
plt.figure(figsize=(7, 7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title('Distribution of Resting Heart Rate Categories')
plt.show()
