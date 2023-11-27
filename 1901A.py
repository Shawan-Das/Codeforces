for _ in range(int(input())):
    n,m = map(int,input().split(" "))
    data= list(map(int, input().split(" ")))
    
    distance = [data[0]]
    
    for i in range(1,n):
        distance.append(data[i]-data[i-1])
    distance.append(2*(m-data[-1]))
    
    print(max(distance))
