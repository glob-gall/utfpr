from numpy import*
m = array(eval(input()))
f = array(eval(input()))
ch = array(eval(input()))

vet=zeros(3,dtype=int)
for i in range(size(m)):
	if m[i]>=5.0 and f[i]>=0.75*ch:
		vet[0]=vet[0]+1
	elif m[i]<5.0 and f[i]>=0.75*ch:
		vet[1]=vet[1]+1
	elif m[i]>=5.0 and f[i]<0.75*ch:
		vet[2]=vet[2]+1
print(vet)
