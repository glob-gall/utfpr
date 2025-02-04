from numpy import *

v = array(eval(input()))
v1 = array(eval(input()))

a = 0
i = 0

while(a < size(v1)):
	if v[a] == "ARROZ":
		c = 1.25
	elif v[a] == "FEIJAO":
		c = 2.60
	elif v[a] == "BIS":
		c = 1.80
	elif v[a] == "MIOJO":
		c = 0.85
	elif v[a] == "FANTA":
		c = 3.20

	i = i + (c * v1[a])
	a = a + 1

print(i)
