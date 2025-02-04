a = float(input())
b = float(input())
c = float(input())

print("Entradas: ", a, " ," , b, " ," , c)

if((a < b + c) and (b < a + c) and (c < a + b)):
	if(a == b and b == c and a == c):
		print("Tipo de triangulo: equilatero")
	elif(a == b or b == c):
		print("Tipo de triangulo: isosceles")
	else:
		print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")