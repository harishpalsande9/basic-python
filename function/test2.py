#Return Statement Single Value 
#Defining a Function

def add():
    x = 10
    y = 20
    c = x + y 
    return c
    
add()

sum = add()
print(sum)


def add1(x , y ):
    return x + y
    
sum1 = add1( 10 , 10 )
print(sum1)


def sub():
    a = int(input("Enter First"))
    b = int(input("Enter second"))
    return a  - b
    
print(sub())