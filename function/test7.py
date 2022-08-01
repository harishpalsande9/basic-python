# Anonymous Function Or Lambdas

def show(x):
    print(x)
    
show(5)

show = lambda x : print(x)
show(10)


add = lambda x , y : x + y

print(add(10,10))


# Nested Lambdas Function

sub = lambda x=10 : (lambda  y : x + y)

a = sub()

print(a(20) , "Nested Lambdas")