while True:
    n = int(input("> "))
    for i in range(n):
        print( " "*(n-i)  , "/" , " "*(i*2) , "\\" , sep="")
    print( “-“ * (2*n+1+1) )

