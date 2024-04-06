for _ in range(int(input())):
    i, e, u = map(int, input().split())
    
    iTent = i
    eTent = e // 3
    uTent = (e % 3 + u) // 3
    
    if (e % 3 != 0) and (e%3)+u < 3:
        print(-1)
    else:
        print(iTent + eTent + uTent + ((e % 3 + u) % 3 != 0))
