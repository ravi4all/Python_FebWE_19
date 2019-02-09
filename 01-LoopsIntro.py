'''
range(5) - start = 0, stop = 5, step = 1
range(5,25) - start = 5, stop = 25, step = 1
range(5,25,5) - start = 5, stop = 25, step = 5
'''

for i in range(2,11):
    print(i,"->",i**2)
    print("--------")
print("Loop Exit")
print("Where am I..??")

for i in range(2,21,2):
    print(i)

#Reverse Loop
for i in range(10,1,-1):
    print(i)

for i in reversed(range(1,10)):
    print(i)

