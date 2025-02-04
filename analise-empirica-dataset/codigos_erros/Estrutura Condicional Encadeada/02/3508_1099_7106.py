a = float(input("lado a: "))
b = float(input("lado b: "))
c = float(input("lado c: "))

print("Entradas: ", a, ",", b, ",", c)

if ((a >= b+c) or (b >= c+a) or (c >= a+b)):
	print("Tipo de triangulo: invalido")
	
else:
	if ((a == b) and (b == c) and (c == a)):
		print("Tipo de triangulo: equilatero")
		
	elif ((a==b) or (b== c)):
		print("Tipo de triangulo: isosceles")
		
	else:
		print("Tipo de triangulo: escaleno")
				
			