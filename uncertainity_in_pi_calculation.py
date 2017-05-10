from Calculation_of_pi import *
# the uncertainity in the calculation

def pi_gen():
	l =[]
	for i in range(1000):
		l.append(pi())
	return l
l3 = []
sigma = []
ji = []
for j in range(1000):
	print(j)
	for i in range(j):
		l3.append(pi())
	sig = np.std(l3)
	ji.append(j)
	sigma.append(sig)
plt.plot(ji,sigma, 'blue')
plt.ylabel("The error in the calculation")
plt.xlabel("Number of samples used to calculate pi")
plt.title('The uncertainity in pi calculation')
plt.show()

