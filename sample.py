def function1():
    print("this is simple python program")
    a = input("Type 1 to continue or any other key to exit")
    try:
        a = int(a)
    except:
        exit()
    else:
        if a == 1:
            print("Program continued, thank you")
        else:
            exit()

if __name__ == "__main__":
    function1()