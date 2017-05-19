
# the uncertainity in the calculation
import numpy as np
import matplotlib.pylab as plt
def pi(n):
    a = 0
    for i in range(n):
        x = np.random.uniform(-1,1)
        y = np.random.uniform(-1,1)
        if x**2 +y**2 <=1:
            a += 1
    return (a/n)*4
n = []    
for i in range(10,10010,100):
	n.append(i) 
print(n)	
	   
sigma = []
for i in n:
	print(i)
	l3 = []
	for j in range(1000):
		l3.append(pi(i))
	sig = np.std(l3)
	sigma.append(sig)
#plt.plot(n,sigma, 'blue')
#plt.ylabel("The error in the calculation")
#plt.xlabel("Number of samples used to calculate pi")
#plt.title('The uncertainity in pi calculation')
#plt.show()

plt.semilogx(n, sigma, 'blue')
plt.ylabel("The error in the calculation")
plt.xlabel("Number of samples used to calculate pi")
plt.title('The uncertainity in pi calculation')
plt.show()


