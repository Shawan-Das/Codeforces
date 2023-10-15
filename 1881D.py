def add_divs(x, divs):
    i = 2
    while i * i <= x:
        while x % i == 0:
            if i in divs.keys():
                divs[i] += 1
            else:
                divs[i] = 1
            x //= i
        i += 1
    if x > 1:
        if x in divs:
            divs[x] += 1
        else:
            divs[x] = 1
    
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    if a.count(a[0])==n:
        print('YES')
        continue
    
    divs = {}
    for x in a:
        add_divs(x, divs)
    flag= True
    for e in divs.values():
        if e % n != 0:
            flag=False
            break
    if flag: print('YES')
    else: print('NO')
