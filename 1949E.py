n,m = map(int, input().split(" "))
health = list(map(int, input().split(" ")))

a,b = m//2, m-(m//2)

if (max(health)>a and max(health)>b) or max(health)==a:
    print(a,b)
else :
    print(b,a)