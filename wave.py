while True:
    n= int(input("> "))
    for i in range(n,-n-1,-1):
        print(" "*(i**2),"*",sep="")

