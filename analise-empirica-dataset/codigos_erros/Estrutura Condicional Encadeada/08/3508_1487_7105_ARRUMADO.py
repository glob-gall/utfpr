nome = input()
quantidade = int(input())

if quantidade > 0 and quantidade <= 50:
    if nome == "ARROZ":
        gramas = quantidade * 500
        print(gramas)
    elif nome == "CENOURA":
        gramas = quantidade * 100
        print(gramas)
    elif nome == "KAMPYO":
        gramas = quantidade * 20
        print(gramas)
    elif nome == "NORI":
        gramas = quantidade * 50
        print(gramas)
    elif nome == "OMELETE":
        gramas = quantidade * 200
        print(gramas)
    elif nome == "PEPINO":
        gramas = quantidade * 150
        print(gramas)
    elif nome == "SALMAO":
        gramas = quantidade * 300
        print(gramas)
    elif nome == "SHITAKE":
        gramas = quantidade * 150
        print(gramas)
    else:
        print("Nome inválido")
else:
    print("Entrada inválida")
