n = int(input("Digite o valor de n: "))
v = zeros(n, dtype=float)
for i in range(1, n + 1):
    if i % 2 == 0:
        v[i - 1] = -1 / i
    else:
        v[i - 1] = 1 / i
H = round(sum(v), 6)
print("H =", H)
