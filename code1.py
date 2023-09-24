x,y=0,1

for t in range(int(input())): 
    data=list(map(int,input().split(' ')))
    a,b=data[:2],data[2:]
    if(a[x]==b[x] and a[y]==b[y]): step=0
    elif(a[y]==b[y] and b[x]<a[x]): step= a[x]-b[x]
    else:
        step= b[y]-a[y]
        a[x]+= step
        a[y]+= step
        if(a[x]>b[x]): step+= a[x]-b[x]
        else: step=-1
    print(step)