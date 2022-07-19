from numpy import *
stu_roll = array([101,102,103,104,105,106])

n = len(stu_roll)
for ele in range(n):
    print(ele , "=" , stu_roll[ele])
    
    
print("Whith While loop")

n = len(stu_roll)
i = 0
while i < n :
    print(stu_roll[i])
    i+=1