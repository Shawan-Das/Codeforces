def swap_position_check(x,y,i):
    
    max_prod = int(x)*int(y)
    
    if i == len(x)-1:
        t_x = x[:i]+y[i]
        t_y = y[:i]+x[i]
    else:
        t_x = x[:i]+y[i]+x[i+1:]
        t_y = y[:i]+x[i]+y[i+1:]
    
    temp_max_prod = int(t_x)*int(t_y)
    
    if max_prod > temp_max_prod:
        return x,y
    else :
        return t_x, t_y

for _ in range(int(input())):
    x = input()
    y = input()
    
    change = [i for i in range(len(x)) if x[i]!=y[i]]
    
    if len(change)==0:
        print(x)
        print(y)
        continue
    if len(x)==1:
        print(x)
        print(y)
        continue
    if len(x)==2 :
        x,y = swap_position_check(x,y,1)
        print(x)
        print(y)
        continue
    # print(type(change[0]))
    for i in change:
        x,y = swap_position_check(x,y,i)
        
    print(x)
    print(y)
    
    
    
def another_solve():
    for _ in range(int(input())):
        x = input()
        y = input()
        n = len(x)
        f = False
        x_list = list(x)
        y_list = list(y)
        for i in range(n):
            if (x_list[i] > y_list[i]) == f:
                x_list[i], y_list[i] = y_list[i], x_list[i]
            f |= (x_list[i] != y_list[i])
        print("".join(x_list))
        print("".join(y_list))