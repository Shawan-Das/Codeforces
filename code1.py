for _ in range(int(input())):
    n,k,x=map(int,input().split(" "))

    r=n-k
    minTotal,maxTotal =(k*(k+1))//2 , ((n*(n+1))//2)-(r*(r+1)//2)

    if(minTotal<=x and x<=maxTotal): print("Yes")
    else: print("NO")