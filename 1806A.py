for t in range(int(input())): 
    a,b,c,d=map(int,input().split(' '))
    if b<=d and c<=a+d-b :
        var= (d-b)+(a+d-b-c)
        print(var)
    else: print(-1)