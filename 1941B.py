def solve(number):
    for i in range(len(number)-2):
        if number[i]==0:
            continue
        if number[i]<0:
            print("NO")
            return
        number[i], number[i+1], number[i+2] = 0, number[i+1]-(2*number[i]), number[i+2]-number[i]
        
        if number[i+1]<0 or number[i+2] < 0:
            print("NO")
            return
    
    if (number[-1] != 0 or number[-2] != 0) :
        print("NO")
    else :
        print("YES")

for _ in range(int(input())):
    n = int(input())
    number = list(map(int, input().split()))
    
    if n== number.count(0):
        print("YES")
        continue
    
    if n==3 and number[0]==number[2] and 2*number[0]== number[1]:
        print("YES")
        continue
    elif n == 3:
        print("NO")
        continue
    
    solve(number)
        