def partition(data, low, high):
    pivot = data[high]
    i = low-1
    
    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    
    data[i+1], data[high] = data[high], data[i+1]
    
    return i+1

def quickSort(data, low, high):
    if low < high:
        pi = partition(data, low, high)
        quickSort(data, low, pi-1)
        quickSort(data, pi+1, high)
        

n = int(input())
data= list(map(int, input().split(" ")))

quickSort(data,0,n-1)

print(data)