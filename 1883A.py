d={1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 0:10}

for _ in range(int(input())):
    n= input()
    time = 4 + abs(d[int(n[0])] - d[1]) + abs(d[int(n[0])] - d[int(n[1])]) + abs(d[int(n[1])] - d[int(n[2])]) + abs(d[int(n[2])] - d[int(n[3])])
    
    print(time)