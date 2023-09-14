# data1=[100, 23, 53, 11, 56, 31]
# data2=[1245, 31, 12, 6, 6, 6]
# data1=[1,2,3,4,5,6,7]
# data2=[7,6,5,4,3,2,1]
a,b=6,2
i=0
while(True):
    c= abs(a-b)
    i+=1
    if(c==0): break
    a=b
    b=c
print(i&3)
