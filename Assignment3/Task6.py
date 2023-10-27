def partition(data,low,high):
    pivot = data[high]
    i = low-1
    
    for j in range(low, high):
        if data[j]< pivot:
            i +=1
            data[i], data[j]= data[j], data[i]
    data[i+1], data[high] = data[high], data[i+1]
    return i+1

def quick_select(data, low, high, k):
    if low == high:
        return data[low]
    pivot_index = (low+high)//2
    
    data[pivot_index], data[high] = data[high], data[pivot_index]
    partition_index= partition(data, low, high)
    
    if k == partition_index: return data[k]
    elif k < partition_index: return quick_select(data, low, partition_index-1, k)
    else: return quick_select(data, partition_index+1, high, k)
    


n = int(input())
data= list(map(int, input().split(" ")))

for _  in range(int(input())):
    k= int(input())
    
    result = quick_select(data,0,n-1,k-1)
    
    print(result)