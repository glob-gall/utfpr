from numpy import*
notas = array(eval(input()))
fr =array(eval(input()))
ch = int(input())
fa = ch*75/100
s = zeros(3,dtype=int)

for i in range(size(notas)):

	if( notas[i]>= 5 and fr[i]>= fa):
		s[0]+=1
	elif(notas[i]< 5 and fr[i]>= fa):
		s[1]+=1

	elif(notas[i]>= 5 and fr[i]< fa):
		s[2]+=1
		
print(s)
		
		
	
	
	
