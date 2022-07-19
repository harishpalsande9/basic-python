print("Numpy One Dimensional Array using linspace Function")

from numpy import *

a = linspace(1 , 8,5)
print(a)

n = len(a)

for i in range(n):
    print('index' , i , '=' , a[i])

print()