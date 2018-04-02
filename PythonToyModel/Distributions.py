import numpy as np
###################################################################################################################################################
def E(alpha= 0.5):
    while True:
        x = np.random.uniform(0,10)
        y = np.random.uniform(-alpha,0)
        f = alpha*np.exp(-alpha*x)
        if y <=f:
            return x
##############################################################################################################
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
