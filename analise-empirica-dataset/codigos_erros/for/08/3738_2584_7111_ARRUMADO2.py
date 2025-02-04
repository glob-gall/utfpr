N = int(input("N: "))

k = 0
sinal = 1
for i in range(1, N + 1):
    k = k + (sinal * (1 / i))
    sinal = -sinal
print("H =", round(k, 6))
