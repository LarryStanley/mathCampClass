for y in range(3,-4,-1):
    for x in range(-10,10):
        if x==y**3:
            print("*",end="")
        else:
            print(" ",end="")
    print()

