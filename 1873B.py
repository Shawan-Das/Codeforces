for _ in range(int(input())):
    n= int(input())
    data= list(map(int, input().split(" ")))
    
    data.sort()
    data[0] +=1
    product=1
    
    for d in data:
        product *= d
    print(product)