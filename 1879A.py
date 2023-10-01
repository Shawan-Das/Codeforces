s,e=0,1
for _ in range(int(input())):
    data=[]
    for i in range(int(input())):
        t=list(map(int,input().split(" ")))
        if(i!=0 and t[e]<data[0][e]): continue
        data.append(t)

    f= data[0]
    flag=True
    for d in data[1:]:
        if(d[s]>=f[s] and d[e]>=f[e]):
            flag=False
            break
    
    if(flag): print(f[s])
    else: print(-1)
