import math

for _ in range(int(input())):
    n= int(input())
    
    ans= int(math.sqrt(n))
    
    while ans**2 > n: ans -=1
    
    while ans**2 < n: ans += 1
    
    print(ans-1)