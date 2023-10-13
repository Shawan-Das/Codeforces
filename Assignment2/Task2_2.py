input_text= "input2.txt"
output_text= "output2.txt"
output = open(output_text,'w')
text= open(input_text,'r')
n=int(text.readline())
dataN= list(map(int,text.readline().split(" ")))
m=int(text.readline())
dataM= list(map(int,text.readline().split(" ")))
text.close()

data=[]
i,j=0,0

while(i<n and j<m):
    if(dataN[i]<dataM[j]):
        data.append(dataN[i])
        i+=1
    else:
        data.append(dataM[j])
        j+=1

while(i<n):
    data.append(dataN[i])
    i+=1
while(j<m):
    data.append(dataM[j])
    j+=1

output_text=""   
for d in data:
    output_text+=str(d)+" "

output.writelines(output_text)
output.close()




#dataN, dataM
i,j=0,0

while (i<n and j<m):
    if dataN[i]<dataM[j]:
        data.append(dataN[i])
        i+1
    else:
        data.append(dataM[j])
        j+1

while(i<n):
    data.append(dataN[i])
    i+=1
    
while(j<m):
    data.append(dataM[j])
    j+=1
