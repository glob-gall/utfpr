from numpy import*

p = array(eval(input()))
q = array(eval(input()))

i = 0
t = 0

while(i < size(q)):
	
	if(p[i] == "ARROZ"):
		
		c = 1.25
		
	elif(p[i] == 'FEIJAO'):
		
		c = 2.60
		
	elif(p[i] == 'BIS'):
		
		c = 1.80
		
	elif(p[i] == 'MIOJO'):
		
		c = 0.85
		
	elif(p[i] == 'FANTA'):
		
		c = 3.20
	
	t = t + c * q[i]
	
	i = i + 1
	
print(t)

