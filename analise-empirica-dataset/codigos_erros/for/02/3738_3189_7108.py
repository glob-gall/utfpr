from numpy import*
mf= array(eval(input()))
p= array(eval(input()))
ch= int(input())
cont= zeros(3,dtype=int)

for a in range(size(mf)):
	if mf[a]>=5.0 and p[a]>=0.75*ch:
		cont[0]= cont[0]+1
	
	elif mf[a]<5.0 and p[a]>=0.75*ch:
		cont[1]= cont[1]+1
		
	elif mf[a]>=5.0 and p[a]<0.75*ch:
		cont[2]= cont[2]+1
	
print(cont)
		 
	




		
		
		
		