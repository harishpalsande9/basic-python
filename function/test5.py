print("Function return another Function")
print()

def disp():
    def show():
        return "Show Function"
    print("Disp Function")
    return show
    
r_sh = disp()

print(r_sh())