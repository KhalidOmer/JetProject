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
plt.title('The inverse transform method')
plt.xlabel('The angle Theta(in radians)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
L = []
stand = []
num = []
for i in range(1000):
	print(i)
	for j in range(i):
		L.append(theta())
	stand.append(np.std(L))
	num.append(i)

plt.plot(num, stand, color ='b')
plt.xlabel('Number of samples')
plt.ylabel('The error in the calculation')
plt.title('The Error in the Calculation')
plt.show()
