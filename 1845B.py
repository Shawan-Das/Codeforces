def samePoint(a,x):
    if(a[0]==x[0] and a[1]==x[1]): return True
    else: return False

def distance(X,A):
    distanceX= abs(X[0]-A[0])
    distanceY= abs(X[1]-A[1])
    return distanceX+distanceY

for t in range(int(input())):
    x,y=0,1
    A= list(map(int,input().split(" ")))
    B= list(map(int,input().split(" ")))
    C= list(map(int,input().split(" ")))

    count=(distance(A,B)+distance(A,C)-distance(B,C))//2
    print(count+1)
    
    