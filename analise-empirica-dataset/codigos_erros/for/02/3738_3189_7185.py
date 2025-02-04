from numpy import *

# Inputs

medias = array(eval(input()))
freq = array(eval(input()))
ch = int(input())

# Vetor nominal

nom = zeros (3, dtype = int)

# Loop

for i in range(size(medias)):
	
	if (freq[i] < (ch * 0.75)):
		
		nom[2] = nom[2] + 1
		
	if (medias[i] < 5.0):
		
		nom[1] = nom[1] + 1
		
	

nom[0] = size(medias) - (nom[1] + nom[2])
print (nom)