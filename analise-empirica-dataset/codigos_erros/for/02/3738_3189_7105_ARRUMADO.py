import numpy as np

medias = np.array(eval(input()))
pres = np.array(eval(input()))
ch = int(input())
ap = 0
repf = 0
repn = 0
vf = np.zeros(3, dtype=int)
vff = []

for x in pres:
    if x < 0.75 * ch:
        repf += 1
    else:
        ap += 1

for x in medias:
    if x < 5:
        repn += 1
    else:
        ap += 1

vff.append(ap)
vff.append(repn)
vff.append(repf)

print(vff)
