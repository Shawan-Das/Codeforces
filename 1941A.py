def count_smaller_numbers(arr, w):
    left = 0
    right = len(arr) - 1
    count = 0

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] <= w:
            count = mid + 1  # Include the current index
            left = mid + 1
        else:
            right = mid - 1

    return count

for _ in range(int(input())):
    n,m,k = map(int, input().split())
    n_coin = list(map(int, input().split()))
    m_coin = list(map(int, input().split()))
    
    n_filter = [i for i in n_coin if i <k]
    m_filter = [i for i in m_coin if i <k]
    n_coin, m_coin = n_filter, m_filter
    n_coin.sort()
    m_coin.sort()
    combination = 0 
    for i in  n_coin:
        combination += count_smaller_numbers(m_coin, k-i)  
    print(combination)