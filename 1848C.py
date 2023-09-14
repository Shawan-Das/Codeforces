def checkCase(a,b):
    n=len(a)
    if(a==b):
        print("YES")
        return True
    elif(sum(a)==0 or sum(b)==0):
        print("YES")
        return True
    return False


testcase=int(input())
for t in range(testcase):
    n = int(input())
    memory=[]
    a=list(map(int, input().split(" ")))
    b=list(map(int, input().split(" ")))
    
    if(a==b): print("YES")
    elif(a.count(0)==n or b.count(0)==n): print("YES")
    else:
        flag=False
        for j in range(max(sum(a),sum(b))) :
            c=[]
            for k in range(len(a)):
                c.append(abs(a[k]-b[k]))
            if(c in memory):
                print("NO")
                memory.clear()
                flag=True
                break
            a=b
            b=c
            if(checkCase(a,b)):
                flag=True
                break
        if(flag==False): print("NO")