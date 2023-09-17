def totalChips(a):
    count=0
    for i in range(len(a)-1):
        count += abs(sum(a[i+1: ])-(len(a[i+1: ])*a[i]))
    return count 

def ChipsStack(d,a):
    temp=str(a)
    
    if(temp in d.keys()):
        return d,d[temp]
    else:
        d[temp]=totalChips(a)
        return d,d[temp]

test=int(input())
d={}
for t in range(test):
    n,m= map(int,input().split(" "))
    
    data=[]
    for j in range(n):
        temp= list(map(int,input().split(" ")))
        data.append(temp)
    data2=[]
    for i in range(m):
        temp2=[data[j][i] for j in range(n)]
        temp2.sort()
        data2.append(temp2)
    data=data2
    
    noOfChips=0
    if(n==1):
        print(0)
        continue
    
    for i in range(len(data)):
        if(sum(data[i])==0):
            continue
        elif(data[i].count(data[i][0])==len(data[i])):
            continue
        else:
            d,v = ChipsStack(d,data[i])
            noOfChips+=v
    print(noOfChips) 
    