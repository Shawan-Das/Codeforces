for _ in range(int(input())):
    
    n,k = map(int, input().split(" "))
    data=list(map(int, input().split(" ")))
    
    bad=0
    for i in range(n):
        data[i] -=1
        
        if data[i]%k != i%k: bad+=1
        
    if(bad==0): print(0)
    elif(bad==2): print(1)
    else: print(-1)