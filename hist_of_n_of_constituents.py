import pickle

import matplotlib.pylab as plt
f = open('data1.pickle', 'rb')
n = pickle.load(f)
k = pickle.load(f)
m = pickle.load(f)



plt.hist([n, k, m], bins=30, histtype='step',label=['R=1', 'R=.1', 'R=.05'], fill = False, cumulative = False, stacked = True, color=['blue', 'green', 'red'])
plt.xlabel('Number of constituents')
plt.ylabel('Frequency')
plt.text(300,100,'This the number of constituents in the Jet with highest energy', color ='red', fontsize=8, bbox = {'facecolor': 'white', 'pad':9}, verticalalignment='top', horizontalalignment='center')
plt.text(350,130,'p = -1', color = 'blue', bbox= {'facecolor': 'white', 'pad':10})
plt.title('Number of Constituents in a Jet')
plt.legend(loc='upper right')
plt.show()
