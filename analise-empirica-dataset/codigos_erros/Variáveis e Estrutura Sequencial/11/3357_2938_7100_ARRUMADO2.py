import math

# Entrada de dados
a = float(input("Distância entre o observador e a primeira árvore: "))
b = float(input("Distância entre o observador e a segunda árvore: "))
gamma = float(input("Ângulo entre a e b (em graus): "))

# Conversão do ângulo para radianos
gamma_rad = math.radians(gamma)

# Cálculo da distância c usando a lei dos cossenos
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(gamma_rad))

# Saída do resultado com duas casas decimais
print("Distância entre as duas árvores: {:.2f}".format(c))
# print("{:.2f}".format(c))
