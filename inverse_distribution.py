import numpy as np
import matplotlib.pylab as plt
def theta():
    eps = 0.01
    while True:
        x = np.random.uniform(0,np.pi*.5)
        y = np.random.uniform(0,1/eps)
        f = 1/(eps+x)
        if y <= f:
            return x
l =[]
for i in range(1000):
    l.append(theta())
plt.hist(l,bins=200,label = '1000 samples',color='b')
#plt.title('The inverse transform method')
plt.xlabel('The values of x')
plt.ylabel('Frequency')
plt.legend()
plt.show()

