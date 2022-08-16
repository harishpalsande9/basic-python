# Local Variables 

def add(y):
    x = 10
    print(x + y)
    
add(10)

# Global Variables

a = 10

def sub(b):
    print(a-b)
    
sub(5)

# Global Function

x = 50
def show():
    a = 10
    print("Local Variable A : " , a)
    x = globals()['a']
    print("X : " , x)
    x = 40
    print("X :",x)
    
    
show()
print("Global Variable  A :" , a)