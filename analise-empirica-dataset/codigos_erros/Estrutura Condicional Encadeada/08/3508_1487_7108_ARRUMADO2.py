nome_ingrediente = input()
quantidade_receitas = int(input())

if quantidade_receitas < 1 or quantidade_receitas > 50:
    print("Entrada invalida")
else:
    if nome_ingrediente == "ARROZ":
        quantidade_ingrediente = quantidade_receitas * 500
        print(quantidade_ingrediente)
    elif nome_ingrediente == "CENOURA":
        quantidade_ingrediente = quantidade_receitas * 100
        print(quantidade_ingrediente)
    elif nome_ingrediente == "KAMPYO":
        quantidade_ingrediente = quantidade_receitas * 20
        print(quantidade_ingrediente)
    elif nome_ingrediente == "NORI":
        quantidade_ingrediente = quantidade_receitas * 50
        print(quantidade_ingrediente)
    elif nome_ingrediente == "OMELETE":
        quantidade_ingrediente = quantidade_receitas * 200
        print(quantidade_ingrediente)
    elif nome_ingrediente == "PEPINO":
        quantidade_ingrediente = quantidade_receitas * 150
        print(quantidade_ingrediente)
    elif nome_ingrediente == "SALMAO":
        quantidade_ingrediente = quantidade_receitas * 300
        print(quantidade_ingrediente)
    elif nome_ingrediente == "SHITAKE":
        quantidade_ingrediente = quantidade_receitas * 150
        print(quantidade_ingrediente)
    else:
        print("Entrada invalida")
