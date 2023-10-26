def merge(data, l,m, r):
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

def merge_sort(data, l,r):
    if(l<r):
        m= (l+r)//2
        merge_sort(data,l,m)
        merge_sort(data,m+1,r)
        merge(data,l,m,r)
        
n = int(input())
data= list(map(int, input().split(" ")))

if n==1:
    print(data)
else:
    merge_sort(data,0,n-1)
    print(data)