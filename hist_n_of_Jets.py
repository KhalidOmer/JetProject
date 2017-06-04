import pickle

import matplotlib.pylab as plt
f = open('data2.pickle', 'rb')
n = pickle.load(f)
k = pickle.load(f)
m = pickle.load(f)

print('R=1', n, sep='\n')
print('R=.1', k, sep='\n')
print('R=.05', m, sep='\n')


plt.hist([n, k, m], bins=30, histtype='step',label=['R=1', 'R=.1', 'R=.05'], fill = False, cumulative = False, stacked = False, color=['blue', 'green', 'red'])
plt.xlabel('Number of Jets')
plt.ylabel('Frequency')
#plt.text(50,25,'This the number of constituents in the Jet with highest energy', color ='red', fontsize=8, bbox = {'facecolor': 'white', 'pad':9}, verticalalignment='top', horizontalalignment='center')
plt.text(600,900,'p = -1', color = 'blue', bbox= {'facecolor': 'white', 'pad':10})
plt.title('Number of Jets')
plt.legend(loc='upper right')
plt.show()
