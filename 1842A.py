test= int(input())
for i in range(test):
    n,m=map(int,input().split(" "))
    
    tsondu= list(map(int,input().split(" ")))
    tenzing= list(map(int, input().split(" ")))
    
    if(sum(tsondu)==sum(tenzing)): print("Draw")
    elif(sum(tsondu)>sum(tenzing)): print("Tsondu")
    else: print("Tenzing")