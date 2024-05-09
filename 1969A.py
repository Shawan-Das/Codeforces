for _ in range(int(input())):
    n= int(input())
    data = list(map(int, input().split()))
    
    if n== 2:
        print(2)
        continue
    p = [i-1 for i in data]
    ans = 3
    for i in range(n):
        if p[p[i]] == i:
            ans =2
    
    print(ans)
        