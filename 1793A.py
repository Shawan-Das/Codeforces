for _ in range(int(input())):
    d1,d2=map(int,input().split(" "))
    n,m=map(int,input().split(" "))

    buy= n//(m+1)
    remain= n- buy*(m+1)
    
    day2= remain*min(d1,d2)
    day1= buy* min(d1*m, d2*(m+1))
    
    print(day1+day2)