for _ in range(int(input())):
    a,b,m = map(int, input().split(" "))
    
    ans = (m//a) + (m//b) + 2
    
    print(ans)