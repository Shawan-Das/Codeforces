test= int(input())

for t in range(test):
    n=int(input())
    data=list(map(int, input().split(" ")))
    
    count0,count1,prod,Sum=0,0,1,sum(data)
    
    for d in data:
        prod*=d
        if(d==1): count0+=1
        else: count1+=1
    
    if(Sum>=0 and prod==1):
        print(0)
        continue
    if(Sum==0 and count1%2==0):
        print(2)
        continue
    if(Sum>=0 and count1%2==1):
        print(1)
        continue
    
    if(count1%2==0):
        remain=count1-count0
        if(remain%4==0): print(remain//2)
        elif(remain%2==0): print((remain//2)+1)
        else: 
            var=(remain+1)//2
            if(var%2==0): print(var)
            else: print(var+1)
    else:
        remain=count1-count0
        if(remain%4==0): print((remain//2)+1)
        elif(remain%2==0): print(remain//2)
        else:
            var=(remain+1)//2
            if(var%2==1): print(var)
            else: print(var+1)