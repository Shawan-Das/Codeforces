for _ in range(int(input())):
    n, k = map(int,input().split(" "))
    a= list(map(int,input().split(" ")))
    
    S, sum_value, cur,P = 0,0,0, 10**9 +7
    
    for i in range(n):
        sum_value += a[i]
        cur += a[i]
        cur = max(cur,0)
        S = max(S, cur)
    sum_value = (sum_value % P + P)%P
    S = S % P
    t = pow(2,k,P)
    ans = (sum_value + S * t - S + P) % P
    
    print(ans)
    