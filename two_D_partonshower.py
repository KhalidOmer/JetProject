import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


#The new distribution of Z:(1/x)
def Z():
	while True:
    		x = np.random.uniform(0.25,.75)
    		y = np.random.uniform(0,10000)
    		f = 1/(x+0.0001)
    		if y <= f:
    			return x
#@@@##############################################################
#The new distribution of theta(1/x)
def theta():
	while True:
    		x = np.random.uniform(0,np.pi*.5)
    		y = np.random.uniform(0,10000)
    		f = 1/(0.0001+x)
    		if y <= f:
    			return x
############################################################    	
#This part gererates the parton shower   	
E = 1
P_i = np.array([E,E,0,0])
i = 0
xb = np.array([0,0])
xf = np.array([1,0])
l = [(P_i,xb,xf)]#here a list contains(appends) the 4-momentum and the positions 
#where xb refers to the beginning position and xf to the final position which together gives me a line 
while i < len(l):
    P, xb , xf = l[i]
    if P[0] >= .09:#here is the stability limit
        z = Z()
        ang = theta()
        P_r = z*(np.array([P[0], P[1]*np.cos(ang)-P[2]*np.sin(ang), P[1]*np.sin(ang)+P[2]*np.cos(ang),0]))
        P_part = P - P_r
        xbr = xf 
        xbp = xf
        xfr = xf + P_r[1:3]/norm(P_r[1:3])
        xfp = xf + P_part[1:3]/norm(P_part[1:3])
        l.append((P_r,xbr,xfr))
        l.append((P_part,xbp,xfp))
    i +=1
print(l)
# For the 2-d plot 
#first i make a list of the lines out from the big list
d = []
for i in l:
    d.append((i[1], i[2]))
c = [list(i) for i in d] 

#now we plot those lines

ax = plt.axes()
ax.set_xlim(0, 10)
ax.set_ylim(-4,4)
line_segments = LineCollection(c, linewidths=([i[0][0] for i in l]), linestyle='solid')
ax.add_collection(line_segments)
plt.show()


