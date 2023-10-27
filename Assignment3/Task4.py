def find_max(arr):
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[mid:])

    return max(left_max, right_max)

n = int(input())
data= list(map(int, input().split(" ")))

max_value, index= 0,0

for i in range(1,n):
    if data[i]**2 >= max_value: max_value,index = data[i]**2, i

max_i=find_max(data[:index])

print(max_value+max_i)        


