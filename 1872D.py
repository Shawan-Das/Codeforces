import math
testCase= int(input())
for i in range(testCase):
    n,x,y=input().split(" ")
    n=int(n)
    x=sx=int(x)
    y=sy=int(y)
    gcd= math.gcd(x,y)
    lcm = (x*y)//gcd
    var= n//lcm
    countX= (n//x)-var
    countY= (n//y)-var
    
    totalSum=(n*(n+1))//2
    xSum=((n-countX)*(n-countX+1))//2
    ySum=(countY*(countY+1))//2
    
    print((totalSum-xSum)-ySum)
