import sys

for _ in range(int(input())):
    n = int(input())
    p = 1
    while p * 2 <= n:
        p <<= 1
    print(p)
