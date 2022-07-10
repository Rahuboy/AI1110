import numpy as np
import mpmath as mp
import scipy
import matplotlib.pyplot as plt
import functions as fp

maxrange=50
maxlim=11.0
x = np.linspace(0,maxlim,maxrange)#points on the x axis
xx = np.linspace(0,maxlim,maxrange*50) #more points on the x axis

a = []

for i in range(1,11):
	a.append(i*1)

vec_proberr2 = np.vectorize(fp.proberr2, otypes=[np.float])

plt.plot(np.array(a), np.loadtxt('proberr_graph.dat',dtype='double'),'o') #plotting proberr graph
plt.plot(xx,vec_proberr2(xx))

plt.grid() #creating the grid
plt.xlabel('$\gamma$')
plt.ylabel('$P_e(\gamma)$')
plt.legend(["Numerical","Theory"])

plt.show() #opening the plot window