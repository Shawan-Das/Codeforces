for _ in range(int(input())):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    
    dx = max(a[0],b[0],c[0],d[0]) - min(a[0],b[0],c[0],d[0])
    
    print(dx**2)