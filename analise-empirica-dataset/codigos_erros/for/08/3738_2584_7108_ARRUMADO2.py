n = int(input())
h = 0

for i in range(1, n+1):
    if i % 2 == 0:
        h -= 1 / i
    else:
        h += 1 / i

print("H = {:.6f}".format(h))
