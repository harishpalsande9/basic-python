name = "    HarishPalsande    "
str1 = name.lstrip()
str2 = name.rstrip()
str3 = name.strip()
print(name)
print(str1)
print(str2)
print(str3)

print()
print("replace split and join String Functions")

name = "HarishPalsande"
old = "Harish"
new = "New"
namenew = name.replace(old  , new)
namenew1 = name.replace("Palsande"  , "ritesh")
print(namenew)
print(namenew1)
print()
print("Split")


name = "Hello how are you"
print(name)
str1 = name.split(' ')
print(str1)

print()
print("join")

name = ('Hello' , 'How' , 'Are' , 'You')
str1 = '_'.join(name)
print(name)
print(str1)

