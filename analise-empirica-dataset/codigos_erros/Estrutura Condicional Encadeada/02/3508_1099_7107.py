l1 = float(input())
l2 = float(input())
l3 = float(input())

print("Entradas: ",l1, " ,",l2, " ,", l3)

if((l1 < l2 + l3) and (l2 < l3 + l1) and (l3 < l1 + l2)):
	
	if ((l1 == l2) and (l2 == l3) and (l1 == l3)):

		print("Tipo de triangulo: equilatero")
		
	elif(l1 == l2 or l2 == l3):
			
		print("Tipo de triangulo: isosceles")
	   		
	else:
			
		print("Tipo de triangulo: escaleno")
	   		
else:
	
	print("Tipo de triangulo: invalido")