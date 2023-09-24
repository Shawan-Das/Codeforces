a,b=0,1
for t in range(int(input())):
    data=[]
    for i in range(int(input())):
        data.append(list(map(int,input().split(" "))))
    
    count=[d for d in data if d[a]>d[b]]
    
    print(len(count))
    