def samePoint(a,x):
    if(a[0]==x[0] and a[1]==x[1]): return True
    else: return False

def left_right(a,x):
    if(x[0]>a[0]): return 'right'
    else: return 'left'

def up_down(a,x):
    if(x[1]>a[1]): return 'up'
    else: return 'down'

def sameX(a,x):
    if(a[0]==x[0]): return True
    else: return False

def sameY(a,y):
    if(a[1]==y[1]): return True
    else: return False


x,y,count=0,1,"something else"
A= list(map(int,input().split(" ")))
B= list(map(int,input().split(" ")))
C= list(map(int,input().split(" ")))

if(samePoint(A,B) or samePoint(A,C)): count=1  # same point

elif(sameX(A,B) and sameX(A,C)): # same X position
    if(up_down(A,B) != up_down(A,C)) : count=1
    elif(up_down(A,B)=='up'): count= abs(A[y]-min(B[y],C[y]))+1
    else: count= abs(A[y]-max(B[y],C[y]))+1

elif(sameY(A,B) and sameY(A,C)): # same Y position
    if(left_right(A,B) != left_right(A,C)) : count=1
    elif(left_right(A,B)=='right'): count= abs(A[x]-min(B[x],C[x]))+1
    else: count= abs(A[x]-max(B[x],C[x]))+1


# elif(xa==xb and xc==xb): count= abs(ya-min(yb,yc))+1
# elif((xa==xb and ya==yb) or (xa==xc and ya==yc)): count=1
# elif(() or ())