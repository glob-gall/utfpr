a = float(input())
b = float(input())
c = float(input())

print("Entrada:")
print(a, b, c)

if a == b and b == c:
    print("Saída: equilatero")
elif a == b or b == c or a == c:
    print("Saída: isosceles")
else:
    print("Saída: escaleno")
