for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split(" ")))
    d=[]
    if(a[0]!=1): d.append(1)
    else: d.append(2)

    for i in range(1,len(a)):
        var= d[-1]+1
        if var==a[i]: var +=1
        d.append(var)

    print(d[-1])