n= input("Qual o nome do ingrediente?")
qr= int(input("Qual a quantidade de receitas?"))

if (n!="ARROZ") or (n!="CENOURA") or (n!="KAMPYO") or (n!="NORI") or (n!="OMELETE") or (n!="PEPINO") or (n!="SALMAO") or (n!="SHITAKE"):
	k= "Entrada invalida"
if (qr<0) or (qr>50):
	k="Entrada invalida"
else:
	if (n=="ARROZ"):
		k=qr*500
	elif (n=="CENOURA"):
		k=qr*100
	elif (n=="KAMPYO"):
		k=qr*20
	elif (n=="NORI"):
		k=qr*50
	elif (n=="OMELETE"):
		k=qr*200
	elif (n=="PEPINO"):
		k=qr*150
	elif (n=="SALMAO"):
		k=qr*300
	elif (n=="SHITAKE"):
		k=qr*150
print(k)
	