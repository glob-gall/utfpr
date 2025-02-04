import math

lado_a = float(input("Digite a medida do lado A do triângulo: "))
lado_b = float(input("Digite a medida do lado B do triângulo: "))
lado_c = float(input("Digite a medida do lado C do triângulo: "))

if lado_a > 0 and lado_b > 0 and lado_c > 0 and lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
    # As medidas são válidas, calcula a área do triângulo
    semiperimetro = (lado_a + lado_b + lado_c) / 2
    area = math.sqrt(semiperimetro * (semiperimetro - lado_a) * (semiperimetro - lado_b) * (semiperimetro - lado_c))
    area = round(area, 3)
    print("Area:", area)
else:
    # As medidas não são válidas
    print("Area: invalida")
