a = float(input())
b = float(input())
c = float(input())

print("Entradas:", a, ",", b, ",", c)

if a == b and b == c:
    print("equilatero")
elif a == b or b == c or a == c:
    print("isosceles")
else:
    print("escaleno")
