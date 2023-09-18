test=int(input())
for t in range(test):
    n,m=map(int,input().split(" "))
    d= list(map(int, input().split(" ")))
    data=[]
    for i in range(len(d)):
        temp= d[i]%m
        if(temp==0): temp+=m
        data.append([-temp,i+1])
    data.sort()
    #print(data)
    for d in data:
        print(d[1],end=" ")
    print()