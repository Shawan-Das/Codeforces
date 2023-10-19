def calculate(d1,d2,n):
    data=[ abs(d1[i]-d2[i]) for i in range(n) ]
    return sum(data)

for _ in range(int(input())):
    n,m = map(int,input().split(" "))
    data=[]
    for t in range(n):
        d=list(map(int, input().split(" ")))
        data.append(d)
    if n==1:
        print(0)
        continue
    
    total_chips=[]
    for i in range(n-1):
        for j in range(i+1,n):
            total_chips.append(calculate(data[i],data[j],m))
    
    print(sum(total_chips))        
    
    