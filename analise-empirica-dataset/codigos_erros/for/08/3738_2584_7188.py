from numpy import*
n=int(input())
h = 0

for i in range(n):
	i = i + 1
	h = h - (1 * ((-1) ** i) / i )
print("H = ",round(h,6))