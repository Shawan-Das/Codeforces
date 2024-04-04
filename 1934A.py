for _ in range(int(input())):
    n= int(input())
    d = list(map(int, input().split(" ")))
    
    d.sort()
    
    ans = 2*(d[-1]-d[0]+d[-2]-d[1])
    
    print(ans)