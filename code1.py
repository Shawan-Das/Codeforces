data1=[100, 23, 53, 11, 56, 31]
data2=[1245, 31, 12, 6, 6, 6]
data1=[1,2,3,4,5,6,7]
data2=[7,6,5,4,3,2,1]

for j in range(20):
    data3=[]
    for i in range(len(data1)):
        data3.append(abs(data1[i]-data2[i]))
    data1=data2
    data2=data3
    print(data1,data2)
