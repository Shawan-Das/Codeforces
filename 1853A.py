t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    diff = 1e9
    sorted_array = True

    for i in range(n):
        if i > 0:
            diff = min(nums[i] - nums[i - 1], diff)
            sorted_array = sorted_array and nums[i] >= nums[i - 1]

    if not sorted_array:
        print(0)
    else:
        print(diff // 2 + 1)
