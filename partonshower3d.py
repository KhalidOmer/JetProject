
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import norm
import datetime
import time
import csv

debug = False
###################################################################################################################################################

def Z():
    eps = 0.01
    while True:
        x = np.random.uniform(0,1)
        y = np.random.uniform(0,1/eps)
        f = 1/(x+eps)
        if y <= f:  
            return x


###################################################################################################################################################

def theta():
    eps = 0.01
    while True:
        x = np.random.uniform(0,np.pi*.5)
        y = np.random.uniform(0,1/eps)
        f = 1/(eps+x)
        if y <= f:
            return x


##################################################################################################################################################
#the azimuthal angle 
def phi():
    x = np.random.uniform(0,2*np.pi)
    return x

###################################################################################################################################################
#the function normv retruns the axis of the rotation; the vector u and the function input"vector" form a plane, from which find a vector which is orthogonal to the plane. 
def normv(u):
    v = np.array([1,1,1])
    x = u[1]*v[2] - u[2]*v[1]
    y = u[2]*v[0] - u[0]*v[2]
    z = u[0]*v[1] - u[1]*v[0]
    normv = np.array([x,y,z])/norm(np.array([x,y,z]))
    return normv 

###################################################################################################################################################
#This function returns the rotation matrix; angl here is the angle of rotation, v is the axis of the rotation 
#check wikipedia "https://en.wikipedia.org/wiki/Rotation_matrix"
def rotation(v,angl):
    r = np.array([
        np.cos(angl) + v[0]**2*(1-np.cos(angl)), 
        v[0]*v[1]*(1-np.cos(angl))- v[2]*np.sin(angl), 
        v[0]*v[2]*(1-np.cos(angl))+ v[1]*np.sin(angl),
        v[1]*v[0]*(1-np.cos(angl))+v[2]*np.sin(angl),
        np.cos(angl)+v[1]**2*(1-np.cos(angl)), 
        v[1]*v[2]*(1-np.cos(angl))-v[0]*np.sin(angl),
        v[2]*v[0]*(1-np.cos(angl))-v[1]*np.sin(angl),
        v[2]*v[1]*(1-np.cos(angl))+v[0]*np.sin(angl),
        np.cos(angl)+ v[2]**2*(1-np.cos(angl))])
    return r.reshape(3,3)

###################################################################################################################################################
#the function parton3d returns a list of tuples(l) that every tuple contains informaton of the particle(the for momentum, the initial position and the final position) and d is a flat list of l.
#first the particle is being rotated with angle theta "rot1" then is rotated by angle phi rot2 
def parton3d():
    E = 1
    i = 0
    g = []
    P_i = np.array([E,E,0,0])
    xb = np.array([0,0,0])
    xf = np.array([1,0,0])
    l = [(P_i,xb,xf)]
    while i < len(l):
        P, xb, xf = l[i]
        if P[0] > 0.05:
            z = Z()
            ang1 = theta()
            ang2 = phi()
            n = normv(P[1:])
            rot1 = rotation(n,ang1)
            rot2 = rotation(P[1:]/norm(P[1:]),ang2)
            tmp = np.dot(rot2,np.dot(rot1,P[1:]))
            tmp = P[0]*tmp/norm(tmp)
            a = np.array([P[0]])
            P_r = z*np.concatenate((a,tmp))
            P_part = P - P_r 
            xbr = xf 
            xbp = xf
            xfr = xf + P_r[1:]/norm(P_r[1:])
            xfp = xf + P_part[1:]/norm(P_part[1:])
            l.append((P_r,xbr,xfr))
            l.append((P_part,xbp,xfp))
            g.append((P_r[0],norm(P_r[1:])))
            if debug:
                print(g) #g is a list of tuples to compare E and the momentum of the radiated particle 
        i +=1
    d = []
    for i in l:
        d.append(list(i[0])+list(i[1])+list(i[2]))
    return d

###################################################################################################################################################
# the function parton3d generates a 3D  parton shower
# next we save the data in a csv file
#after we read from the same file to plot a 3D parton shower


d  = parton3d()
t =  time.strftime('%a_%H_%M')
f = "parton" + t +'.csv'
with open(f, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for i in d:
            writer.writerow(i)

fig = plt.figure()
ax = fig.gca(projection ='3d')
with open(f, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
            l = list(map(float, row))
            x1, y1, z1 = l[4:7]
            x2, y2, z2 = l[7:]
            if l[0] >=.8:
                color = 'blue'
            if l[0] >.5 and l[0] < .8:
                color = 'green'
            if l[0] < .5:
                color = 'yellow'
            if l[0] <= .1:
                color = 'red'
            ax.plot([x1,x2],[y1,y2],[z1,z2], color=color, linewidth= 5*l[0])       
a = []
b = []
plt.plot(a,b, label = 'E >= 0.8', color = 'blue')
plt.plot(a,b, label = 'E > 0.5', color = 'green')
plt.plot(a,b, label = 'E < 0.5', color = 'yellow')
plt.plot(a,b, label = 'E < 0.1', color = 'red')
plt.legend(loc = 2)
plt.show()
