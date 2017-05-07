import numpy as np
from numpy.linalg import norm
from Distributions import*
debug = False

###############################################################################

"""the function normv retruns the axis of the rotation; the vector u and 
the function input"vector" form a plane, from which find a vector which 
is orthogonal to the plane. 
"""
def normv(u):
    v = np.array([1,1,1])
    x = u[1]*v[2] - u[2]*v[1]
    y = u[2]*v[0] - u[0]*v[2]
    z = u[0]*v[1] - u[1]*v[0]
    normv = np.array([x,y,z])/norm(np.array([x,y,z]))
    return normv 

###############################################################################
#This function returns the rotation matrix; angl here is the angle of rotation, 
#v is the axis of the rotation 
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

###############################################################################
"""the function parton3d returns a list of tuples(l) that every tuple contains
informaton of the particle(the for momentum, the initial position and the final
position) and d is a flat list of l.
first the particle is being rotated with angle theta "rot1" then is rotated by 
angle phi rot2"""

def parton3d(P_i):
    i = 0
    xb = np.array([0,0,0])
    xf = P_i[1:]/norm(P_i[1:])
    l = [(P_i,xb,xf)]
    Hadron = []     #list of final state particles
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
            if debug:
                print('P_r: ', P_r[0],norm(P_r[1:]))
                print('P_part:', P_part[0], norm(P_part[1:])) 
        else:
            Hadron.append(P)
        i +=1
    d = []
    for i in l:
        d.append(list(i[0])+list(i[1])+list(i[2]))
    return Hadron


######

def partons(P_i):
    J1 = parton3d(P_i)
    P_d = [1,-1,-1,-1]*P_i
    J2 = parton3d(P_d)
    return J1 + J2

