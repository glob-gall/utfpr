from numpy import*
a= int(input("Numero(N): "))
b= 0

for i in range (1,(a + 1)):
	s= (-1)**(i-1)
	b= s/i+b
	
print("H = ",round(b,6))