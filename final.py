while True :
    n = int( input("> ") )
    print( n , "=" , end=" " )
    for x in range(2,n+1) :
        while n%x == 0 :
            print( x , end=" " )
            n /= x
    print()

