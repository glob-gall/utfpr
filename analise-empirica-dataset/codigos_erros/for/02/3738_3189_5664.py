from numpy import *

m = array(eval(input()))
p = array(eval(input()))
c = int(input())

cont = zeros(3, dtype=int)
f= c*75/100 
for i in range(size(m)):
	if (m[i] >= 5 and p[i] >= f):
		cont[0] = cont[0] + 1
	elif (m[i] <5 ):
		cont[1] = cont[1] + 1
	elif (p[i] < f ):
		cont[2] = cont[2] + 1

print(cont)
