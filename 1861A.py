for t in range(int(input())):
    n=input()
    new=""
    for i in n:
        if i=='1'or i=='3'or i=='7': new+=i
        if(len(new)==2): break
    print(new)