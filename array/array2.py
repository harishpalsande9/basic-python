from array import *
stu_roll = array('i' , [101,102,103,104,105])
print("Original Array")
n = len(stu_roll)
for i in range(n):
    print(i , "=" , stu_roll[i])
    
print("After Slicing")
a = stu_roll[1:3]

for i in a:
    print(i)