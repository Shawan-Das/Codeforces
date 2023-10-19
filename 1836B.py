for _ in range(int(input())):
    n, k, g = map(int, input().split(" "))
    
    stolen = min((g - 1)//2*n, k*g)
    rest = (k*g-stolen)%g
    
    if rest > 0:
        stolen -= (g-1)//2
        last = ((g-1)//2+rest)%g
    
        if last*2<g:
            stolen += last
        else:
            stolen -= g-last
    
    print(stolen)
