for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if (a % 2 == 1 and b % 2 == 1) or (a % 2 == 1 and b == 2 * a):
        print("No")
    else:
        print("Yes")