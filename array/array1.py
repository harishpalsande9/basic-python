from array import * 

stu_roll = array('i',[101,102,103,104,105])
print("Remove Method")
for i in stu_roll:
    print(i)
    
print("Array After Remove")
stu_roll.remove(101)
for i in stu_roll:
    print(i)

print("index Method")
stu_roll = array('i',[101,102,103,104,105])

print(stu_roll.index(105))


print("Reverse Method")
stu_roll = array('i',[101,102,103,104,105])
stu_roll.reverse()

for i in stu_roll:
    print(i)

print("Extend Method")
stu_roll = array('i',[101,102,103,104,105])
tech_roll = array('i',[201,202,203,204,205])
stu_roll.extend(tech_roll)

for i in stu_roll:
    print(i)