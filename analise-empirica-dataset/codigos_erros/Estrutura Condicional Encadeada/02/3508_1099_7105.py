# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades 
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

print("Entradas: ", a ,", ", b, ", ", c)

if((a>0 and b>0 and c>0) and (((a+b)>c) and (b+c)>a and (a+c)>b)) :
	if(a == b and b ==c):
		print("Tipo de triangulo: equilatero")
	elif((a == b and c != b and c !=a) or (a == c and c != b and b !=a) or (c == b and a != b and c !=a)):
		print("Tipo de triangulo: isosceles")
	else:
		print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")