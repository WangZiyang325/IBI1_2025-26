a=508         # the estimated population of Scotland in 2004
b=533         # the estimated population of Scotland in 2014
c=555         # the estimated population of Scotland in 2024
d=b-a         # the change in population between 2004 and 2014 
e=c-b         # the change in population between 2014 and 2024
print(d,e)
print(d>=e)   # d > e population growth is decelerating in Scotland


A=1==1
B=1==2
X = A
Y = A 
W = X or Y
print('W1 is',W)
X = A
Y = B 
W = X or Y
print('W2 is',W)
X = B
Y = A 
W = X or Y
print('W3 is',W) 
X = B
Y = B 
W = X or Y
print('W4 is',W)    


# X = True, Y = True, W = True
# X = True, Y = False, W = True
# X = False, Y = True, W = True
# X = False, Y = False, W = False