for y in range(5,-6,-1):
    for x in range(-5,6):
        if x==y:
            print("*",end="")
        elif x==-y:
            print("+",end="")
        else:
            print(" ",end="")
    print()

