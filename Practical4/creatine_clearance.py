# input the value of age, weight, gender and Cr
# check whether the value is in correct ranges, if not, print the error place
# calculate CrCl, and print the result

age = int(input("Enter age (years): "))                        # input age
weight = float(input("Enter weight (kg): "))                   # input weight
gender = input("Enter gender (M/F): ")                         # input gender
Cr = float(input("Enter creatine concentration (μmol/l): "))   # input Cr

if age <= 0 or age >= 100:
    print("Error: Age is not in the correct range (0-100).")  # check age rang
if weight <= 20 or weight >= 80:
    print("Error: Weight is not in the correct range (20-80 kg).")  # check weight
if gender != 'M' and gender != 'F':
    print("Error: Gender must be 'M' or 'F'.")  # check gender
if Cr <= 0 or Cr >= 100:
    print("Error: Creatine concentration is not in the correct range (0-100 μmol/l).")  # check Cr

if 0 < age < 100 and 20 < weight < 80 and gender in ['M', 'F']:
    if gender == 'M':
        CrCl = ((140 - age) * weight) / (72 * Cr)  # calculate Cr
    elif gender == 'F':
        CrCl = ((140 - age) * weight) / (72 * Cr) * 0.85  # calculate Cr
    print("Creatine clearance (CrCl) is:", CrCl, "ml/min")  # print result
