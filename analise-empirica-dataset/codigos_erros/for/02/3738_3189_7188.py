from numpy import*
me= array(eval(input()))
p= array(eval(input()))
ch= array(eval(input()))

vet=zeros(3,dtype=int)
for i in range(size(me)):
	if me[i]>=5.0 and p[i]>=0.75*ch:
		vet[0]=vet[0]+1
	elif me[i]<5.0 and p[i]>=0.75*ch:
		vet[1]=vet[1]+1
	elif me[i]>=5.0 and p[i]<0.75*ch:
		vet[2]=vet[2]+1
print(vet)
