nome = input()
quantidade = int(input())

if (quantidade <=0 or quantidade > 50):
	q = "Entrada invalida"
else:
	if (nome=="ARROZ"):
		q  = quantidade*500
	elif (nome == "CENOURA"):
		q = quantidade *100
	elif (nome == "KAMPYO"):
		q = quantidade*20
	elif (nome == "NORI"):
		q = quantidade *50
	elif (nome == "OMELETE"):
		q = quantidade*200
	elif (nome == "PEPINO"):
		q = quantidade *150
	elif (nome == "SALMAO"):
		q = quantidade*300
	elif (nome == "SHITAKE"):
		q = quantidade*150
print(q)