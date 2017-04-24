import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import norm
import csv


###################################################################################################################################################

def Z():
    while True:
        x = np.random.uniform(0.25,.75)
        y = np.random.uniform(0,10000)
        f = 1/(x+0.0001)
        if y <= f:  
            return x


###################################################################################################################################################

def theta():
    while True:
        x = np.random.uniform(0,np.pi*.5)
        y = np.random.uniform(0,10000)
        f = 1/(0.0001+x)
        if y <= f:
            return x


##################################################################################################################################################
#the azimuthal angle 
def phi():
    x = np.random.uniform(0,2*np.pi)
    return x

###################################################################################################################################################
#this function here calculates the axis of the rotation; the vector u and the function input"vector" form a plane, from which we find our axis of rotation 
def normv(v):
    u = np.array([1,1,1])
    x = u[1]*v[2] - u[2]*v[1]
    y = u[2]*v[0] - u[0]*v[2]
    z = u[0]*v[1] - u[1]*v[0]
    normv = np.array([x,y,z])/norm(np.array([x,y,z,0]))
    return normv 

###################################################################################################################################################
#This function returns the rotation matrix; angl here is the angle of rotation 
def rotation(v,angl):
    r = np.array([np.cos(angl) + v[0]**2*(1-np.cos(angl)), v[0]*v[1]*(1-np.cos(angl))- v[2]*np.sin(angl), v[0]*v[2]*(1-np.cos(angl))+ v[1]*np.sin(angl),
                v[1]*v[0]*(1-np.cos(angl))+v[2]*np.sin(angl), np.cos(angl)+v[1]**2*(1-np.cos(angl)), v[1]*v[2]*(1-np.cos(angl))-v[0]*np.sin(angl),
                 v[2]*v[0]*(1-np.cos(angl))-v[1]*np.sin(angl),v[2]*v[1]*(1-np.cos(angl))+v[0]*np.sin(angl), np.cos(angl)+ v[2]**2*(1-np.cos(angl))])
    return r.reshape(3,3)

###################################################################################################################################################

def parton3d():
    E = 1
    i = 0
    P_i = np.array([E,E,0,0])
    xb = np.array([0,0,0])
    xf = np.array([1,0,0])
    l = [(P_i,xb,xf)]
    while i < len(l):
        P, xb, xf = l[i]
        if P[0] > 0.09:
            z = Z()
            ang1 = theta()
            ang2 = phi()
            n = normv(P[1:])
            rot1 = rotation(n,ang1)
            rot2 = rotation(P[1:],phi())
            tmp = np.dot(rot2,np.dot(rot1,P[1:]))
            a = np.array([P[0]])
            P_r = z*np.concatenate((a,tmp))
            P_part = P - P_r 
            xbr = xf 
            xbp = xf
            xfr = xf + P_r[1:]/norm(P_r[1:])
            xfp = xf + P_part[1:]/norm(P_part[1:])
            l.append((P_r,xbr,xfr))
            l.append((P_part,xbp,xfp))
        i +=1
    d = []
    for i in l:
        d.append(list(i[0])+list(i[1])+list(i[2]))
    return d

###################################################################################################################################################
# the function above generates a 3D  parton shower
# next we save the data in a csv file
#after we read from the same file to plot a 3D parton shower


d  = parton3d()
with open("parton.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for i in d:
            writer.writerow(i)

fig = plt.figure()
ax = fig.gca(projection ='3d')
ax.set_xlim3d(-4, 10)
ax.set_ylim3d(-3,5)
ax.set_zlim3d(-3,2)
with open('parton.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        l = list(map(float, row))
        x1 = l[4]
        y1 = l[5]
        z1 = l[6]
        x2 = l[7]
        y2 = l[8]
        z2 = l[9]
        if l[0] >=.8:
            color = 'red'
        if l[0] >.5 and l[0] < .8:
            color = 'yellow'
        if l[0] < .5:
            color = 'magenta'
        if l[0] <= .1:
            color = 'blue'
        ax.plot([x1,x2],[y1,y2],[z1,z2], color=color, linewidth=l[0])
plt.show()

