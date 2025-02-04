from numpy import*
x=int(input("x:"))
y=0
c=1
for i in range(1,x+1):
	y=y+c/i
	c=-c
print("H = ",(round(y,6)))