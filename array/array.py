#Create array Example 1
#import array as *
from array import *

print("Create array Example 1") 

stu_roll = array('i' , [ 101 , 102 , 103 , 104 , 105])

stu_roll1 = [ 101.3 , 102 , 103 , 104 , 105]

print(stu_roll[0])
print(stu_roll1[0])


#Create array Example 2
print("Print Example 2 Accessing Array using for Loop Array Module")

for el in stu_roll:
    print(el)

print("--------")

n = len(stu_roll)
#range(n)
#print(n)

for i in range(n):
    print(i , "=" ,stu_roll[i])

#Accessing Array using while Loop Array Module
print("----------------------------------------")
print("Accessing Array using while Loop Array Module")

n = len(stu_roll)
i = 0
while (i<n):
    print(stu_roll[i])
    i+=1
    
#append() method
print("append-----------------------------")
for e in stu_roll:
    print(e)

print("after Array append Method ")
stu_roll.append(106)
#print(stu_roll)

for e in stu_roll:
    print(e)
    
    
    
#Getting Array input from user using for Loop in Python 

print("Getting Array input from user using for Loop in Python ")

stu_roll = array("i",[])
n = int(input("Enter Number of Elements : "))

for i in range(n):
   stu_roll.append(int(input("Enter Element : ")))

for i in range(len(stu_roll)):
    print(stu_roll[i])
    
# Pop 

stu_list = array("i",[1,2,3,4,5])
stu_list.pop()

for i in stu_list:
    print(i)
  