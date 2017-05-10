import pickle

import matplotlib.pylab as plt
f = open('data.pickle', 'rb')
n = pickle.load(f)
k = pickle.load(f)
m = pickle.load(f)



plt.hist([n, k, m], bins=30, histtype='step',label=['R=1', 'R=.1', 'R=.05'], fill = False, cumulative = False, stacked = True, color=['blue', 'green', 'red'])
plt.xlabel('Pseudomass')
plt.ylabel('Frequency')
plt.text(.0020,100,'this histogram represents the pseudomass of the jets with more than one constituent', color ='red', fontsize=8, bbox = {'facecolor': 'white', 'pad':9}, verticalalignment='top', horizontalalignment='center')
plt.text(0.0020,130,'p = -1', color = 'blue', bbox= {'facecolor': 'white', 'pad':10})
plt.title('Pseudomass Observable')
plt.legend(loc='upper right')
plt.show()
