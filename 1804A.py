for _ in range(int(input())):
    a,b=map(int,input().split(" "))
    
    a,b=abs(a),abs(b)
    
    if(a==b): print(a+b)
    else: print(2*max(a,b)-1)