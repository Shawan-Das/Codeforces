def find_max(arr):
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[mid:])

    return max(left_max, right_max)


n = int(input())
data= list(map(int, input().split(" ")))

max_number= find_max(data)
print(max_number)

## time complexity: 
# The divide and conquer algorithm I provided for finding the maximum number in an unsorted
# list has a time complexity of O(n), where n is the length of the list. 
# This is because the algorithm recursively divides the list into smaller halves until it reaches lists of length 1, 
# and in the process, it examines each element exactly once.

# The reason for this linear time complexity is that the algorithm doesn't
# perform redundant comparisons. It keeps track of the maximum element found in each subproblem and combines these maximums
# efficiently. Therefore, the time it takes to find the maximum does not grow significantly as the size of the input list (n) increases.