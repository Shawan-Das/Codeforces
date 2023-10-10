def merge(arr, l,m, r):
    i,j= l,m+1
    temp_data=[]
    while(i<=m and j<=r):
        if(data[i]<data[j]):
            temp_data.append(data[i])
            i+=1
        else:
            temp_data.append(data[j])
            j+=1
    
    while(i<=m):
        temp_data.append(data[i])
        i+=1
    while(j<=r):
        temp_data.append(data[j])
        j+=1
    data[l:r+1]=temp_data[:]


def mergeSort(data, l,r):
    if(l<r):
        m= (l+r)//2
        mergeSort(data,l,m)
        mergeSort(data,m+1,r)
        merge(data,l,m,r)


input_text= "input2.txt"
output_text= "output2.txt"
output = open(output_text,'w')
text= open(input_text,'r')
n=int(text.readline())
dataN= list(map(int,text.readline().split(" ")))
m=int(text.readline())
dataM= list(map(int,text.readline().split(" ")))
text.close()

data= dataN + dataM

mergeSort(data,0, len(data)-1)

output_text=""

for d in data:
    output_text+=str(d)+" "

output.writelines(output_text)
output.close()