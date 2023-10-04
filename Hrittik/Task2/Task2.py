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
    print('-1-',arr)
    print('-2-',temp)
    arr[left:right+1]=temp[:]
    print('-3-',arr)
def merge_sort(arr,left,right):
    
    if(left<right):
        mid=(left+right)//2
        merge_sort(arr,left,mid)
        merge_sort(arr,mid+1,right)
        merge(arr,left,mid,right)


data=[(7, 40), (4, 50), (9, 50), (3, 20), (2, 10), (5, 10), (1, 10)]
merge_sort(data,0,len(data)-1)
print(data)