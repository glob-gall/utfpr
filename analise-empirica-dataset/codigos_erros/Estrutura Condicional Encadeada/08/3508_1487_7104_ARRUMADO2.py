nome = input()
quantidade = int(input())

ingredientes = {
    "ARROZ": 500,
    "CENOURA": 100,
    "KAMPYO": 20,
    "NORI": 50,
    "OMELETE": 200,
    "PEPINO": 150,
    "SALMAO": 300,
    "SHITAKE": 150
}

if quantidade < 1 or quantidade > 50 or nome not in ingredientes:
    print("Entrada invalida")
else:
    q = ingredientes[nome] * quantidade
    print(q)
