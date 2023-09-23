for t in range(int(input())):
    n,k = map(int, input().split(" "))
    flag= False
    
    for y in range(2):
        var= n-(k*y)
        if(var>=0 and var%2==0):
            flag= True
            break
    if(flag): print("Yes")
    else: print("No")