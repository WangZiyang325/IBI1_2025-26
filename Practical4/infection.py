# 1.Set initial values: 5 infected, 40% daily growth rate, start at day 1
# 2. Loop while infected number < 91
# 3. In loop: save current infected number, calculate new infected number
# 4. If new number ≥91, set to 91
# 5. Add 1 to day count, print new infected people and current day
# 6. After loop, print total days to reach 91 infected





n=5  # initial population
v=0.4  # daily growth rate (40%)
day=1  # starting day
while n<91:
    a=n
    n=n*(1+v)
    if n>=91:
        n=91
    day=day+1
    print('new individuals added:',n-a,'on day:',day)
print('It needs',day,'days for the population to be 91.') 

