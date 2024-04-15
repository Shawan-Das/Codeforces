for _ in range(int(input())):
    n= int(input())
    data = list(map(int, input().split()))
    has_remainder_1 = any(x%3 ==1 for x in data)
    if sum(data)%3 == 0 :
        print(0)
    elif n==1 or sum(data)%3 in data or sum(data)%3 == 2:
        print(1)
    elif has_remainder_1:
        print(1)
    else :
        print(2)