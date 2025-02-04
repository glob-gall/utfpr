a= float(input())
b= float(input())
c= float(input())

if(a>0 and b>0 and c>0):
		
	if (a<(b+c) and b<(a+c) and c<(a+b)):		
	
		if(a==b==c):
			print("Entradas:",a,b,c)
			print("Tipo de triangulo: equilatero")
		
		elif(a==b or a==c or b==c):
			print("Entradas:",a,",",b,",",c)
			print("Tipo de triangulo: isosceles")
		
		else:
			print("Entradas:",a,",",b,",",c)
			print("Tipo de triangulo: escaleno")
			
	else:
		print("Entradas:",a,",",b,",",c)
		print("Tipo de triangulo: invalido")
	
else:
	print("Entradas:",a,",",b,",",c)
	print("Tipo de triangulo: invalido")

	
