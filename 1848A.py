for _ in range(int(input())):
    
    n,m,k = map(int, input().split(" "))
    x, y= map(int, input().split(" "))
    temp= (x+y)%2
    ans = "Yes"
    
    for i in range(k):
        x1,y1= map(int, input().split(" "))
        if (x1+y1)%2== temp: ans= 'No'
    
    print(ans)