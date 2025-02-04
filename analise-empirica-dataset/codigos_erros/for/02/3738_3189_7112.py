from numpy import*

a = array(eval(input()))
b = array(eval(input()))
c = float(input())

CH = (0.75)*c

Vet = zeros(3, dtype= int)

for i in range(size(a)):
	
	if(a[i] >= 5.0) and (b[i]>= CH):
		Vet[0] = Vet[0] + 1
	if(a[i] < 5.0):
		Vet[1] = Vet[1] +1
	if(b[i] < CH ):
		Vet[2] = Vet[2] +1 
	

print(Vet)
