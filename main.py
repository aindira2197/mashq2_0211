# 1
n = int(input())
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print(fib[:n])

# 2
matn = input().split()
print(max(matn, key=len))

# 3
lst = list(map(int, input().split()))
print(sorted(lst, reverse=True))

# 4
import math
r = float(input())
print(math.pi * r * r)

# 5
parol = input()
print(len(parol) >= 8 and any(i.isdigit() for i in parol))
