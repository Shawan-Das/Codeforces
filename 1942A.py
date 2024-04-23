for _ in range(int(input())):
    n,k = map(int, input().split(" "))
    
    if k==1:
        data = [i+1 for i in range(n)]
    elif k==n:
        data= [1 for i in range(n)]
    else:
        data = [-1]
        
    result = ' '.join(map(str, data))
    print(result)