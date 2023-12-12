t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = n * (n + 1) // 2

    if a[-1] != x:
        a.append(x)
        b = [a[i] - a[i - 1] for i in range(1, n)]  # Calculate the differences
        print("YES" if len(set(b)) == n - 1 and all(1 <= x <= n for x in b) else "NO")
        continue

    cnt = {}
    cnt[a[0]] = 1
    for i in range(1, n - 1):
        cnt[a[i] - a[i - 1]] = cnt.get(a[i] - a[i - 1], 0) + 1

    cnt_gt_1 = [p for p in cnt if cnt[p] > 1]
    if len(cnt_gt_1) > 1 or (len(cnt_gt_1) == 1 and cnt[cnt_gt_1[0]] > 2):
        print("NO")
        continue

    cnt_0 = [i for i in range(1, n + 1) if i not in cnt]
    print("YES" if len(cnt_0) == 2 else "NO")
