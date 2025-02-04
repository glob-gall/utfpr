import numpy as np

n = int(input())
h = 0

for i in range(1, n+1):
    h = h + (-1) ** i / i

print("H =", round(h, 6))
