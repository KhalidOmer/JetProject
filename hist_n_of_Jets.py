import pickle

import matplotlib.pylab as plt
f = open('data2.pickle', 'rb')
n = pickle.load(f)
k = pickle.load(f)
m = pickle.load(f)


plt.hist([n, k, m], bins=30, histtype='step',label=['R=1', 'R=.1', 'R=.05'], fill = False, cumulative = False, stacked = True, color=['blue', 'green', 'red'])
plt.xlabel('Number of Jets')
plt.ylabel('Frequency')
#plt.text(50,25,'This the number of constituents in the Jet with highest energy', color ='red', fontsize=8, bbox = {'facecolor': 'white', 'pad':9}, verticalalignment='top', horizontalalignment='center')
plt.text(700,80,'p = -1', color = 'blue', bbox= {'facecolor': 'white', 'pad':10})
plt.title('Number of Jets')
plt.legend(loc='upper right')
plt.show()
