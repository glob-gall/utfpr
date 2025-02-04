lado_a = float(input("Digite a medida do lado A do triângulo: "))
lado_b = float(input("Digite a medida do lado B do triângulo: "))
lado_c = float(input("Digite a medida do lado C do triângulo: "))

if lado_a == lado_b == lado_c:
    print("equilatero")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("isosceles")
else:
    print("escaleno")
