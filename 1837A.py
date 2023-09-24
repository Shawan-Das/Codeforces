for t in range(int(input())):
    x,k= map(int,input().split(" "))
    data=[]

    if(k>x): data=[x]
    elif(x%k != 0): data=[x]
    else: data=[1,x-1]

    print(len(data))
    for d in data: print(d,end=" ")
    print()