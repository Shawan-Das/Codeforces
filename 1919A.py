winner= ["Bob", "Alice"]
for _ in range(int(input())):
    a,b = map(int, input().split())
    print(winner[(a+b)%2])
    