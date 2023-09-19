test=int(input())

for t in range(test):
    n=int(input())
    data=list(map(int, input().split(" ")))
    numbers=[i+1 for i in range(n)]
    total= (n*(n+1))//2
    if(data[-1]>total):
        print("NO")
        continue
    
    if(total != data[-1]): 
        data.append(total)
        
        if(data[0] not in numbers):
            print("NO")
            continue
        numbers.remove(data[0])    
        for i in range(1,n):
            var = data[i]-data[i-1]
            if(var in numbers): numbers.remove(data[i]-data[i-1])
            else: break
        if(len(numbers)==0): print("YES")
        else: print("NO")
        continue
    
    diff=[]
    
    for i in range(len(data)):
        if(i==0): continue
        else: 
            var= data[i]-data[i-1]
            if(var in numbers): numbers.remove(var) 
            else: diff.append(var)
    if(len(diff)==0): diff.append(data[0])
    elif(data[0] in numbers): numbers.remove(data[0])
    if(len(numbers)>2): print("NO")
    elif(len(diff)>1): print("NO")
    elif(numbers[0]+numbers[1]==diff[0]): print("YES")
    else: print("NO")
    