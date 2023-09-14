def countF(data, s,e):
    count=0
    for d in data:
        for i in range(s,e+1):
            if(i>=d[0] and i<=d[1]): count=count+1
        
    return count
    

test= int(input())
for t in range(test):
    n= int(input())
    a=list(map(int, input().split(" ")))
    
    s=min(a)
    e=max(a)
    sm=[]
    for i in range(n):
        data=[]
        for j in range(n):
            if a[i]<a[j]: data.append([a[i],a[j]])
            else: data.append([a[j],a[i]])
        sm.append(countF(data,s,e))
        
    for d in sm:
        print(d, end=' ')
    print("")
    
    
    # a[x[i].second]=n+x[i].first*(2*i-n)-s1+s2