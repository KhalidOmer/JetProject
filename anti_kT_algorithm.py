
import heapq
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import norm


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
