
import heapq
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import norm
import datetime
import time
import csv

debug = False
###################################################################################################################################################
def E(alpha= 0.5):
    while True:
        x = np.random.uniform(0,10)
        y = np.random.uniform(-alpha,0)
        f = alpha*np.exp(-alpha*x)
        if y <=f:
            return x
#################################################################################################################################################
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
def parton3d(E):
    i = 0
    P_i = np.array([E,E,0,0])
    xb = np.array([0,0,0])
    xf = np.array([1,0,0])
    l = [(P_i,xb,xf)]
    Hadron = []#list of final state particles
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
########################################################
#partons concatenates two parton showers
def partons(E):
    J1 = parton3d(E)
    J2 = parton3d(-E)
    return J1 + J2
########################################################
class Pseudojet:
    instances  = []
    def __init__(self, v_momentum):
        self.momentum = v_momentum
        self.index = len(Pseudojet.instances)
        self.is_jet = False
        self.exists = True 
        Pseudojet.instances.append(self)
########################################################
def dij(Ji,Jj,p, R):
    Pi = Ji.momentum
    Pj = Jj.momentum
    pTi = np.sqrt(Pi[1]**2 + Pi[2]**2)
    #yi = 1/2 * np.log((Pi[0] + Pi[3])/(Pi[0]-Pi[3]))
    yi = 1/2 * np.log((norm(Pi[1:])+Pi[3])/(norm(Pi[1:])-Pi[3]))
    phii = np.arctan(Pi[2]/Pi[1])
    pTj = np.sqrt(Pj[1]**2 + Pj[2]**2)
    yj = (1/2) * np.log((norm(Pj[1:]) + Pj[3])/(norm(Pj[1:])-Pj[3]))
    phij = np.arctan(Pj[2]/Pj[1])
    Delij = np.sqrt((yi - yj)**2 + (phii - phij)**2)
    mini = min(pTi**(2*p), pTj**(2*p))
    di_j = mini * Delij/R
    if debug:
        if di_j != di_j:
            print("nan", Pi, Pj)
    return di_j 
###########################################################
def diB(Ji, p):
    Pi = Ji.momentum
    pTi = np.sqrt(Pi[1]**2 + Pi[2]**2)
    di_B = pTi**(2*p)
    return di_B
###########################################################
def combine(J1, J2,p,R,H,lis):
    J = J1.momentum + J2.momentum
    J1.exists = False
    J2.exists = False
    J  = Pseudojet(J)
    di_B = diB(J,p)
    heapq.heappush(H,(di_B,J.index,-1))
    for i in range(len(lis)-1):
        if lis[i].exists:
            di_j = dij(J,lis[i],p,R)
            heapq.heappush(H,(di_j,J.index,i))
###########################################################

def jetcluster(p,R,J):
    Pseudojet.instances = []
    for j in J:
        Pseudojet(j)
    lis = Pseudojet.instances
    H =[]
    for i in range(len(lis)):
        di_B = diB(lis[i],p)
        heapq.heappush(H,(di_B,i,-1))
        for j in range(i+1, len(lis)):
            di_j = dij(lis[i],lis[j],p,R)
            heapq.heappush(H,(di_j,i,j))
    d, i, j = heapq.heappop(H)
    if j != -1:
        if lis[i].exists and lis[j].exists:
            combine(lis[i],lis[j],p,R,H,lis)
    else:
        if lis[i].exists:
            lis[i].exists = False
            lis[i].is_jet = True 
    while len(H) !=0:
        d, i, j = heapq.heappop(H)
        if j != -1:
            if lis[i].exists and lis[j].exists:
                combine(lis[i],lis[j],p,R,H,lis)
        else:
            if lis[i].exists:
                lis[i].exists = False
                lis[i].is_jet = True
    a = 0 
    for j in Pseudojet.instances:
        if j.is_jet:
            a+=1
    return a
if __name__ == "__main__":
	l = []
	for i in range(1000):
    		l.append(partons(E()))
	J = []
	for j in l:
		b = jetcluster(-1,1,j)
		J.append(b)

	J1 = []
	for i in l: 
    		J1.append(jetcluster(-1,0.01,i))
    		
	
	J2 =[]
	for i in l:
		J2.append(jetcluster(-1,0.05,i))


	plt.hist(J, bins=200, alpha=0.5, label='R=1')
	plt.hist(J2, bins=200, alpha=0.5, label='R=.05')
	plt.hist(J1, bins=200, alpha=0.5, label ='R=.01')
	plt.xlabel('Number of Jets')
	plt.ylabel('Frequency')
	plt.legend(loc='upper right')
	plt.show()
