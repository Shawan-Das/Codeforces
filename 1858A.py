test=int(input())

for t in range(test):
    a,b,c = input().split(" ")
    a=int(a)
    b=int(b)
    c=int(c)
    
    if(c%2==1): a+=1
    
    if(a==b): print("Second")
    elif(a>b): print("First")
    else: print("Second")