t = int(input())

for _ in range(t):
    n = int(input())
    d = list(map(int, input().split(" ")))

    d.sort()
    dta = [(d[i], d[i + n]) for i in range(n)]
    ans = 0

    for i in range(1, n):
        ans += abs(dta[i][0] - dta[i - 1][0]) + abs(dta[i][1] - dta[i - 1][1])

    print(ans)
    
    for v in dta:
        print(v[0], v[1])
