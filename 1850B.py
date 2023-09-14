def Winner(data1,data2):
    m=-999999999
    iteration=1
    winner=1
    
    for i in range(len(data1)):
        if(data1[i]<=10 and data2[i]>=m):
            m=data2[i]
            winner=i
    print(winner+1)

testCase= int(input())

for i in range(testCase):
    totalItem= int(input())
    data1=[]
    data2=[]
    for j in range(totalItem):
        a,b = input().split(" ")
        data1.append(int(a))
        data2.append(int(b))
    Winner(data1,data2)

