from numpy import*

n= int(input())
d=0

for i in range (1,(n + 1)):
	s= (-1)**(i-1)
	d= s/i+d
	
print("H = ",round(d,6))