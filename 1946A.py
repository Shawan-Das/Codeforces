for _ in range(int(input())):
    n = int(input())
    a= list(map(int,input().split(" ")))
    
    a.sort()
    p = (n+1)//2-1
    res = a[p:].count(a[p])
    
    print(res)