for _ in range(int(input())):
    x, y, k = map(int, input().split())
    if y < x:
      print(x)
    else:
      print(y + max(0, y - x - k))
