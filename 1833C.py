for _ in range(int(input())):
    n= int(input())
    data= list(map(int, input().split(" ")))
    
    if 1 in data: 
        print("YES")
        continue
    data.sort()
    if(data[0]%2==1):
        print('YES')
        continue
    
    for d in data:
        flag=False
        if d%2==1:
            print('NO')
            flag=True
            break
    if flag : continue
    print('YES')    
    