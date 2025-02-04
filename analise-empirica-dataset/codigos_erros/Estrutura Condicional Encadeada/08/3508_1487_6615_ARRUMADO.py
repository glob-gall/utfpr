n = input("Digite o nome do ingrediente: ").upper()
q = int(input("Digite a quantidade de receitas que deseja preparar: "))

if n not in ["ARROZ", "CENOURA", "KAMPYO", "NORI", "OMELETE", "PEPINO", "SALMAO", "SHITAKE"] or q < 0 or q > 50:
    print("Entrada inválida")
else:
    if n == "ARROZ":
        print(q * 500)
    elif n == "CENOURA":
        print(q * 100)
    elif n == "KAMPYO":
        print(q * 20)
    elif n == "NORI":
        print(q * 50)
    elif n == "OMELETE":
        print(q * 200)
    elif n == "PEPINO":
        print(q * 150)
    elif n == "SALMAO":
        print(q * 300)
    elif n == "SHITAKE":
        print(q * 150)
