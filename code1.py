test = int(input())

for t in range(test):
    n=int(input())
    data=list(map(int,  input().split(" ")))
    
    total= (n*(n+1))//2
    
    if(data[-1]>total):
        print("NO")
        continue
    
    if(data[-1] < total):
        data.append(total)
        diff=[data[i]-data[i-1] for i in range(1,n)]
        diff.insert(0,data[0])
        if(sum(set(diff))==total): print("YES")
        else: print("NO")
        continue
    
    else:
        number=[1]*n
        number.insert(0,0)
        diff=[]
        flag=False
        for i in range(len(data)):
            if(i==0): continue
            
            var=data[i]-data[i-1]
            
            if(var==0): 
                flag=True
                break
            if(var>n): diff.append(var)
            elif(number[var]==1): number[var]=0
            elif(number[var]==0): diff.append(var)
            
        if(flag):
            print("NO")
            continue
        if(len(diff)==0): diff.append(data[0])
        else: number[data[0]]=0
        #print(number)
        if(sum(number)!=2):
            print("NO")
            continue
        if(len(diff)>1):
            print("NO")
            continue
        
        g1= number.index(1)
        g2= number.index(1,g1+1)
        
        if(g1+g2==diff[0]): print("YES")
        else: print("NO")
        
        data.clear()
        number.clear()