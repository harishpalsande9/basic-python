print("Function in Python")

def add1():
    print("sum with by hard code values")
    x = 10
    y = 20
    c = x + y
    print(c)
    
def add2():
    print("Sum With Input values")
    x = int(input("Enter First Number : "))
    y = int(input("Enter Second Number : "))
    c = x + y
    print("The Answer Is : ",c)
    
add1()   
add2()