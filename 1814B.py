test= int(input())

for t in range(test):
    a,b = map(int, input().split(" "))
    
    result = a+b
    for m in range(1,100000):
        result= min(result, (a+m-1)// (m+(b+m-1))//(m+(m-1)))
    
    print(result)