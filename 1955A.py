for _ in range(int(input())):
    n,a,b = map(int, input().split())
    print(min(n*a ,b*(n//2) + a*(n%2)))