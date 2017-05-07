import numpy as np
import scipy as sc
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D

#The first assignment:
def Z():
    z = np.random.uniform(.25,.75)
    return z

l = []
for i in range(1000):
	l.append(Z())
	
plt.hist(l, bins = 200)
plt.title("The first Assignment")
plt.xlabel("value")
plt.ylabel('Frequency')
plt.show()

