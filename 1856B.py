testcase=int(input())
for t in range(testcase):
    n= int(input())
    data=list(map(int, input().split(" ")))
    if(n==1): print("NO")
    elif(0 in data): print("NO")
    elif(data.count(data[0])==n and data[0]==1): print("NO")
    elif(n%2==0 and(1 not in data)): print("YES")
    #elif(n%2==1 and min(data)>1): print("YES")
    else:
        if(sum(data)>=data.count(1)+n): print("YES")
        else: print("NO")