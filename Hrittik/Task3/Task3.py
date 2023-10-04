def file_text(data):
    text=""
    
    for d in data:
        text+= f"ID: {d[0]} Mark: {d[1]}\n"
    return text

def merge(arr,left,mid,right):
    i,j=left,mid+1
    temp=[]
    while(i<=mid and j<=right):
        if(arr[i][1]==arr[j][1]):
            if(arr[i][0]<arr[j][0]):
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
        elif(arr[i][1]<arr[j][1]):
            temp.append(arr[j])
            j+=1
        else:
            temp.append(arr[i])
            i+=1
    while(j<=right):
        temp.append(arr[j])
        j+=1
    while(i<=mid):
        temp.append(arr[i])
        i+=1
    arr[left:right+1]=temp[:]
    
def merge_sort(arr,left,right):
    
    if(left<right):
        mid=(left+right)//2
        merge_sort(arr,left,mid)
        merge_sort(arr,mid+1,right)
        merge(arr,left,mid,right)


input_text= 'Task3\input3.txt' # file location
output_text= 'Task3\output3.txt' # output will be saved on this location
text =open(input_text, 'r') # 'r' used to read file data
text= text.read()

n,i,m=text.split('\n')
n=int(n)
Id=list(map(int,i.split(" ")))
marks=list(map(int,m.split(" ")))
data=[(Id[i],marks[i]) for i in range(n)]

merge_sort(data,0,n-1)

output = open(output_text, 'w')
output.write(file_text(data))