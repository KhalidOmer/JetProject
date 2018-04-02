import numpy as np
import scipy as sc
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D


#generating the angle theta using accept-reject method

#The second assignment:
def Pdf(x,mean,stan):
    f = stats.norm.pdf(x,mean,stan)
    return f

#The function accept-reject:
def acc_rej():
    mean = 45.042761
    stan = 26.582525
    while True:
        x = np.random.uniform(0,90)
        y = np.random.uniform(0,0.016)
        f = Pdf(x,mean,stan)
        if y <= f:
            return x

l1 = []
for i in range(1000):
	l1.append(acc_rej())
	
plt.hist(l1, bins = 200)
plt.show()



