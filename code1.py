test=int(input())

for t in range(test):
    n=int(input())
    data=list(map(int, input().split(" ")))
    numbers=[1]*n
    numbers=[0]+numbers
    total= (n*(n+1))//2
    if(data[-1]>total):
        print("NO")
        continue
    
    if(total != data[-1]): 
        data.append(total)
        
        if(numbers[data[0]] == 0 or numbers[data[0]-1]>n):
            print("NO")
            continue
        numbers[data[0]]=0    
        for i in range(1,n):
            var = data[i]-data[i-1]
            if(numbers[var] ==1): numbers[var]=0
            else: break
        if(sum(numbers)==0): print("YES")
        else: print("NO")
        continue
    
    diff=[]
    
    for i in range(len(data)):
        if(i==0): continue
        else: 
            var= data[i]-data[i-1]
            # print("--",var,'--')
            # print("--",numbers,"--")
            if(var>n): diff.append(var)
            elif(numbers[var]==1): numbers[var]=0 
            else: diff.append(var)
    if(len(diff)==0): diff.append(data[0])
    elif(numbers[data[0]] ==1 ): numbers[data[0]] =0
    if(sum(numbers)>2):
        print("NO")
        continue
    elif(len(diff)>1): 
        print("2NO")
        continue
    g1=numbers.index(1)
    g2=numbers.index(1,g1+1)
    if(g1+g2==diff[0]): print("YES")
    else: print("3NO")
    