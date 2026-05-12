# What does this piece of code do?
# Answer: The code is to draw a random number between 1 and 10 ten times and add them together and print the ansmer

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0           # set initial total_rand value to 0
progress=0               # set initial progress value to 0
while progress<10:      
	progress+=1          # executes the task ten times
	n = randint(1,10)    # draw a random number between 1 and 10
	total_rand+=n        # add th ten random number together

print(total_rand)         

