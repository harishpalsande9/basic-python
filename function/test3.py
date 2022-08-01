# Nested Function

def disp():
    def show():
        print("Show Function")
    print("Disp Function")
    show()


disp()
