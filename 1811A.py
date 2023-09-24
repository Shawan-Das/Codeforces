power={}
for i in range(10):
    power[str(i)]=i
    
for t in range(int(input())):
    n,d= map(int,input().split(" "))
    value=input()
    
    for v in  range(len(value)):
        if d> power[value[v]]:
            value= value[:v]+str(d)+value[v:]
            break
    
    if(len(value)==n): value+=str(d)
    print(value)