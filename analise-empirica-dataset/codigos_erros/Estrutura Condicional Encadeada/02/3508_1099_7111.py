# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
A= float (input("Lado A: "))
B= float (input("Lado B: "))
C= float (input("Lado C: "))

print("Entradas: ",A," , ",B," , ",C)
if (A<B+C) and (B<A+C) and (C< A+B):
	if (A==B) and (A==C):
		print("Tipo de triangulo: equilatero")
	elif (A==B or B==C):
		print("Tipo de triangulo: isosceles")
	elif (A!=B) and (B!=C) and (A!=C):
		print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")