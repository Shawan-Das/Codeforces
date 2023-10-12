for _ in range(int(input())):
    n,m,k= map(int, input().split(" "))
    
    if k==1: print(1)
    elif k==2 and m<=n: print(m)
    elif k==2 and m>n : print(n+((m-n)//n))
    elif (k==3 and m<=n) or k>3: print(0)
    elif k==3 and m>n: print((m-n)-((m-n)//n))