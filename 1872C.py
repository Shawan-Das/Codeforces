import math
def validate(l):
    for i in range(3,int(math.sqrt(l))+1,2):
        if(l%i==0): return i
    return l
    

testCase=int(input())
for t in range(testCase):
    l,r=input().split(" ")
    l=int(l)
    r=int(r)
    if(l>r or r<=3): print(-1)
    elif(l==1 and r%2==0): print(2,r-2)
    elif(l==1 and r%2!=0): print(2,r-3)
    elif(l%2==0 and r%2==0):print(2,r-2)
    elif(l%2==0 and r%2!=0): print(2,r-1-2)
    elif(l%2 != 0 and r%2==0): print(2,r-2)
    elif(l%2 !=0 and r%2 !=0 and l!=r): print(2,l-1)
    elif(validate(l)!=l): print(validate(l),l-validate(l))
    else: print(-1)
        
    
#print(data)
#print(len(data))