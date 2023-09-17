test=int(input())

for t in range(test):
    n= int(input())
    data=list(map(int, input().split(" ")))
    
    count=0
    
    for d in range(n):
        if(data[d]==d+1): count+=1
    
    if(count==0): print(0)
    elif(count%2==0): print(count//2)
    else: print((count+1)//2)
    