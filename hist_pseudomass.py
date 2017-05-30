import pickle

def verify_list(L):
	import numpy as np
	XX = np.array([1.0])	
	for i, x in enumerate(L):
		if type(x) != type(XX[0]):
			print(i, x, type(x))
			
def delete_none(L):
	return [x for x in L if x != None]

import matplotlib.pylab as plt
f = open('data3.pickle', 'rb')
n = pickle.load(f)
k = pickle.load(f)
m = pickle.load(f)

for s, L in zip(['n', 'k', 'm'], [n, k, m]): 
	print(s)
	verify_list(L)
p = delete_none(n)
l = delete_none(k)
s = delete_none(m)

plt.hist([p, l, s], bins=30, histtype='step',range = (0,0.002),label=['R=1', 'R=.1', 'R=.05'], fill = False, cumulative = False, stacked = False, color=['blue', 'green', 'red'])
plt.xlabel('Pseudomass (Gev)')
plt.ylabel('Frequency')
#plt.text(.0020,100,'this histogram represents the pseudomass of the jets with more than one constituent', color ='red', fontsize=8, bbox = {'facecolor': 'white', 'pad':9}, verticalalignment='top', horizontalalignment='center')
plt.text(0.004,900,'p = -1', color = 'blue', bbox= {'facecolor': 'white', 'pad':10})
plt.title('Pseudomass Observable')
plt.legend(loc='upper right')
plt.show()
