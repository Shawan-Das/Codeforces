for t in range(int(input())):
    v=input()
    
    if(v[0]=='0'):
        print('0')
        continue
    elif(len(v)==1):
        if(v=="?"): print('9')
        elif(v=='0'): print('0')
        else: print('1')
        continue
    count=1
    mark= v.count('?')
    
    if(v[0]=='?'): count,mark = 9, mark-1
    
    total = count * (10**mark)
    
    print(total)
        