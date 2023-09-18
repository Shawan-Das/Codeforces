test= int(input())

for t in range(test):
    l,r= input().split(" ")
    if(l==r): 
        print(0)
        continue  
    if(len(l)<len(r)): l= '0'*(len(r)-len(l)) + l
    
    for i in range(len(r)):
        if(l[i] != r[i]): 
            print ((int(r[i])-int(l[i]))+9*(len(r)-i-1))
            break