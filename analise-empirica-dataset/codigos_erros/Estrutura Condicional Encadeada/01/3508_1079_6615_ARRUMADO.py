from math import sqrt

a = float(input("lado a: "))
b = float(input("lado b: "))
c = float(input("lado c: "))

print("Entradas:", a, ",", b, ",", c)

if a + b <= c or a + c <= b or b + c <= a or a < 0 or b < 0 or c < 0:
    print("Área: inválida")
else:
    s = (a + b + c) / 2.0
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    print("Área:", round(area, 3))
