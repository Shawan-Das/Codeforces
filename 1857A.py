test=int(input())

for t in range(test):
    n= int(input())
    data=list(map(int,input().split(" ")))
    
    if(n==1): print("NO")
    if(n==2):
        if(data[0]%2==data[1]%2): print("YES")
        else: print("NO")
        continue
    count=0
    for d in data:
        if(d%2==1): count+=1
    
    if(count%2==0): print("YES")
    else: print("NO")