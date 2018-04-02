import pickle

import matplotlib.pylab as plt
f = open('data1.pickle', 'rb')
n = pickle.load(f)
k = pickle.load(f)
m = pickle.load(f)



plt.hist([m, n, k], bins=30, range=(0, 300), histtype='step',label=['R=1', 'R=0.1', 'R=0.05'], fill = False, cumulative = False, stacked = False, color=['blue', 'green', 'red'])
plt.xlabel('Number of constituents')
plt.ylabel('Frequency')
#plt.text(300,1400,'This the number of constituents in the Jet with highest energy', color ='red', fontsize=8, bbox = {'facecolor': 'white', 'pad':9}, verticalalignment='top', horizontalalignment='center')
plt.text(500,1800,'p = -1', color = 'blue', bbox= {'facecolor': 'white', 'pad':10})
plt.title('Number of Constituents in a Jet')
plt.legend(loc='upper right')
plt.show()
