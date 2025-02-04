n = input("digite o nome do ingrediente: ").upper()
q =int(input("digite a quantidade de receitas que deseja preparar: "))
if ((n!="ARROZ") and (n!="CENOURA") and (n!="KAMPYO") and (n!="NORI") and (n!="OMELETE") and (n!="PEPINO") and (n!="SALMAO")and(n!="SHITAKE") and (0>q) or (q>50)):
	print("Entrada invalida")
else:
	if(n=="ARROZ"):
		print(q*500)
	elif(n=="CENOURA"):
		print(q*100)
	elif(n=="KAMPYO"):
		print(q*20)
	elif(n=="NORI"):
		print(q*50)
	elif(n=="OMELETE"):
		print(q*200)
	elif(n=="PEPINO"):
		print(q*150)
	elif(n=="SALMAO"):
		print(q*300)
	elif(n=="SHITAKE"):
		print(q*150)