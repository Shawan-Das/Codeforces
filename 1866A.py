testData=int(input())

data=list(map(int, input().split(" ")))

if(0 in data): print(0)
elif(len(data)==1): print(abs(0-data[0]))
else:
    data.append(0)
    data.sort()
    if(data[0]==0): print(data[1])
    elif(data[-1]==0): print(abs(data[-2]))
    else:  
        index=data.index(0)
        steps= min(abs(data[index-1]-0),abs(data[index+1]-0))
        print(steps)
