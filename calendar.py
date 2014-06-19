#! /usr/bin/python3

monstr = ( "" ,
           "Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" ,
           "Jul" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec" )

wkstr = ( "Sun" , "Mon" , "Tue" , "Wed" , "Thu" , "Fri" , "Sat")

def weekday(y,m,d) :

    if m <= 2 :
        y -= 1
        m += 10
    else :
        m -= 2

    return ( y + y//4 - y//100 + y//400 + int(2.6*m-0.2) + d)% 7


def mdays(y,m) :
    days = (0,31,28,31,30,31,30,31,31,30,31,30,31)
    if m == 2 :
        if y%400 == 0 :
            return 29
        elif y%100 == 0 :
            return 28
        elif y%4 == 0 :
            return 29
        else :
            return 28
    else :
        return days[m]


y = 2014

for m in range(1,13) :
    print( " "*10 , y , monstr[m] )
    for i in range(7) :
        print(" " , wkstr[i] , end="" )
    print()

    a = wk = weekday(y,m,1)
    ymdays = mdays(y,m)

    print( " "*(5*wk) , end="" )
    for d in range(1,ymdays+1) :
        if d<10:
            print("   ", d , end="" )
        if d>9 :
            print("  ", d , end="" )
        if a%7 == 6 :
            print()
        a += 1

    print()
    print()
