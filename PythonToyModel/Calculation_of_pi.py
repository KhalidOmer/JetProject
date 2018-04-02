import numpy as np
import scipy as sc
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D

#Calculation of pi:
def pi():
    a = 0
    for i in range(1000):
        x = np.random.uniform(-1,1)
        y = np.random.uniform(-1,1)
        if x**2 +y**2 <=1:
            a += 1
    return (a/1000)*4

l2=[]
for i in range(1000):
    l2.append(pi())
mu = np.mean(l2)
sigma = np.std(l2)

plt.hist(l2, bins=200, color = 'b', alpha = .5)
plt.title("pi calculation")
plt.xlabel("The approximate value of pi")
plt.ylabel("Frequency")
plt.show()


