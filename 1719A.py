for _ in range(int(input())):
    result = ["Tonya", "Burenka"]
    n, m = map(int, input().split())
    
    print(result[(n+m)%2])