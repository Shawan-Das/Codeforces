import copy

for _ in range(int(input())):
    n= int(input())
    power = list(map(int, input().split()))
    
    while(True):
        old_power = copy.copy(power)
        
        for i in range(1,n):
            power[i] = max(0,power[i]-power[i-1])
        power[0] = max(0, power[0]-power[-1])
        
        if old_power == power :
            break
    
    result = [i+1 for i in range(n) if power[i] != 0]
    string = ' '.join(map(str, result))
    # string = ' '.join([str(i) for i in result]) # may use for any conditions. 
    print(len(result))
    print(string)