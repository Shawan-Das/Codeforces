import math
x,y=0,1

def distance(X,Y):
    return math.sqrt( ((X[x]-Y[x])**2) + ((X[y]-Y[y])**2) )

for _ in range(int(input())):
    O= [0,0]
    P= list(map(int, input().split(" ")))
    A= list(map(int, input().split(" ")))
    B= list(map(int, input().split(" ")))
    
    ob, pa, ab, oa,pb = distance(O,A), distance(P,A), distance(A,B)/2, distance(O,A), distance(P,B)
    ans= max(pa,oa)
    ans= min(ans, max(pb,ob))
    ans= min(ans, max(ab,pa,ob))
    ans= min(ans, max(ab,pb,oa))
    
    print(ans)

    
    print(max(ob,pa,ab))
