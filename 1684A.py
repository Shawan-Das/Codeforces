for _ in range(int(input())):
    n= input()
    
    if len(n)==2:
        print(n[1])
        continue
    data = [int(i) for i in n]
    
    print(min(data))