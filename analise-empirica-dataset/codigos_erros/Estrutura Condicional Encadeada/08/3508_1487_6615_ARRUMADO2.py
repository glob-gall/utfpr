ingrediente = input("Digite o nome do ingrediente: ").upper()
quantidade_receitas = int(input("Digite a quantidade de receitas que deseja preparar: "))

if ingrediente not in ["ARROZ", "CENOURA", "KAMPYO", "NORI", "OMELETE", "PEPINO", "SALMAO", "SHITAKE"] or quantidade_receitas < 1 or quantidade_receitas > 50:
    print("Entrada inválida")
else:
    if ingrediente == "ARROZ":
        quantidade_total = quantidade_receitas * 500
    elif ingrediente == "CENOURA":
        quantidade_total = quantidade_receitas * 100
    elif ingrediente == "KAMPYO":
        quantidade_total = quantidade_receitas * 20
    elif ingrediente == "NORI":
        quantidade_total = quantidade_receitas * 50
    elif ingrediente == "OMELETE":
        quantidade_total = quantidade_receitas * 200
    elif ingrediente == "PEPINO":
        quantidade_total = quantidade_receitas * 150
    elif ingrediente == "SALMAO":
        quantidade_total = quantidade_receitas * 300
    elif ingrediente == "SHITAKE":
        quantidade_total = quantidade_receitas * 150

    print(quantidade_total)
