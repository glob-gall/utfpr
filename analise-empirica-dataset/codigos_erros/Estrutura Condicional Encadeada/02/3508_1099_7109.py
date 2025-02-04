la = float(input("Lado A: "))
lb = float(input("Lado B: "))
lc = float(input("Lado C: "))

print("Entradas: ",la,",",lb,",",lc)
if la < lb+ lc and lb < la+lc and lc < la+lb:
	if la == lb and lb == lc:
		print("Tipo de triangulo: equilatero")
	else:
			if la == lb or lb == lc or lc == la:
				print("Tipo de triangulo: isosceles")
			else:
					print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")
				

