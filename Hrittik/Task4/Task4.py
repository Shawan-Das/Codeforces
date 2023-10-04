def merge(arr,left,mid,right):
    i,j=left,mid+1
    temp=[]
    while(i<=mid and j<=right):
        if(arr[i][0]>arr[j][0]):
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

input_text= 'Task4\input4.txt' # file location
output_text= 'Task4\output4.txt' # output will be saved on this location
text =open(input_text, 'r') # 'r' used to read file data
text= text.read()

temp_data= list(text.split('\n'))
n,temp_data=int(temp_data[0]),temp_data[1:]

data=[]

for td in temp_data:
    train_name, train_info= td.split(' ')[0] ,td
    
    data.append((train_name,train_info))

merge_sort(data,0,n-1)

new_text=""

for d in data:
    new_text+= d[1]+'\n'

output = open(output_text, 'w')
output.write(new_text)