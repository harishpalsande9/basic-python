#Pass Function As Parameter

def disp(sh):
    print("Disp Function" + sh())
    
def show():
    return "Show Function"
    
disp(show)

  