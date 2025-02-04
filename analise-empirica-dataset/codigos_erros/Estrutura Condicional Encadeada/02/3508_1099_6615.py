L1 = float(input("digite o comprimento dum lado: "))
L2 = float(input("digite o comprimento dum outro lado: "))
L3 = float(input("digite o comprimento de mais um lado: "))
print("Entradas: " ,L1,",",L2,",",L3)
if((L1<0) or (L2<0) or (L3<0) or (L1+L2<=L3 or L1+L3<=L2 or L2+L3<=L1)):
	print("Tipo de triangulo: invalido")
else:
	if((L1==L2) and (L1==L3) and (L2==L3)):
		print("Tipo de triangulo: equilatero")
	elif((L1==L2) and (L1!=L3) and (L2!=L3) or (L2==L3 and L2!=L1 and L3!=L1) or (L1==L3 and L1!=L2 and L3!=L2)):
		print("Tipo de triangulo: isosceles")
	elif((L1!=L2) and (L1!=L3) and (L2!=L3)):
		print("Tipo de triangulo: escaleno")