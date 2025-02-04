a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

print("Entradas:", a, ",", b, ",", c)

if a == b == c:
    print("equilatero")
elif a == b or b == c or a == c:
    print("isosceles")
else:
    print("escaleno")
