import math
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
    
    if(checkCase(a,b)==False):
        data=set()
        for i in range(len(a)):
            if(a[i]==b[i] and a[i]==0): continue
            elif(a[i]==b[i]):
                data.add(2)
                continue
            elif(a[i]==0):
                data.add(0)
                continue
            elif(b[i]==0):
                data.add(1)
                continue
            x= b[i]//math.gcd(a[i],b[i])
            y= a[i]//math.gcd(a[i],b[i])
            
            if(x%2 == y%2): data.add(2)
            elif(y%2 == 1): data.add(1)
            else: data.add(0)
        
        if(len(data)<=1): print("YES")
        else: print("NO")
        
        