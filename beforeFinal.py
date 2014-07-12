while True :
    n = int( input("> ") )
    print( n , "有質因數" , end=" " )
    for x in range(2,n+1) :
        if n%x == 0 :
            print( x , end=" " )
            n /= x
    print()

