for _ in range(int(input())):
    n,m = map(int, input().split(" "))
    a = list(input().split(" "))
    # print(a)
    
    zero =[]
    ans = 0
    
    for i in a:
        length = len(i)
        trailing_zero = len(i)- len(i.rstrip('0'))
        zero.append(trailing_zero)
        ans += length - trailing_zero
    
    zero.sort(reverse=True)
    ans += sum(zero[1::2]) #ans += sum(zrr[i] for i in range(1, n, 2))
    print("Sasha" if ans-1 >= m else "Anna")
