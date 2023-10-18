for _ in range(int(input())):
    
    n,k = map(int, input().split(" "))
    value = ((n-1)/k)+1
    if(int(value)<value): print(int(value)+1)
    else: print(int(value))
    