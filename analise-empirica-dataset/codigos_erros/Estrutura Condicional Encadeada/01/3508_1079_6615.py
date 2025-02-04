a= float(input("lado a: "))
b= float(input("lado b: "))
c= float(input("lado c: "))
from math import*
print("Entradas: ", a,",", b,",", c)
if((a+b<=c or a+c<=b or b+c<=a) or (a<0 and b<0 and c<0)):
	s = (a + b + c) / 2.0
	area = sqrt(s * (s-a) * (s-b) * (s-c))
	print("Area: invalida")
else:
		if((a<c and b<c) and (a+b>c)):
			s = ((a + b + c) / 2.0)
			area = sqrt(s * (s-a) * (s-b) * (s-c))
			print("Area: ", round(area,3))
		elif(a<b and c<b) and (a+c>b):
			s = (a + b + c) / 2.0
			area = sqrt(s * (s-a) * (s-b) * (s-c))
			print("Area: ", round(area,3))
		elif((b<a and c<a) and (b+c>a)):
			s = (a + b + c) / 2.0
			area = sqrt(s * (s-a) * (s-b) * (s-c))
			print("Area: ", round(area,3))