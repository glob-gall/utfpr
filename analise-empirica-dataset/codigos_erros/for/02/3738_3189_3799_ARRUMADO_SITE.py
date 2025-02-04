from numpy import *

nvet=array(eval(input()))
fvet=array(eval(input()))
c=float(input())
aux=zeros(3, dtype=int)
ap=0
rpn=0
rpf=0

for i in range(0,size(nvet)):
	if(nvet[i]>=5.0 and fvet[i]>=0.75*c):
		ap=ap+1
	elif(nvet[i]>=5.0 and fvet[i]<0.75*c):
		rpf=rpf+1
	elif(nvet[i]<5.0 and fvet[i]>=0.75*c):
		rpn=rpn+1
aux[0]=ap
aux[1]=rpn
aux[2]=rpf
print(aux)
