#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import math

#if using termux
# import subprocess
# import shlex
#end if


maxrange=30
maxlim=4.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
xx = np.linspace(-maxlim,maxlim,maxrange*5) #more points
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
# randvar = np.loadtxt('uni.dat',dtype='double')
# randvar = np.loadtxt('gau.dat',dtype='double')
randvar = np.loadtxt('log.dat',dtype='double')
for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def unit_cdf(x):
	if(x < 0):
		return 0
	elif(x > 1):
		return 1
	else:
		return x

def gau_cdf(x):
	return((1/2) * (1 + math.erf(x/math.sqrt(2))))

def log_cdf(x):
    if(x < 0):
        return 0
    else:
        return (1 - math.exp(-x/2))


vec_unit_cdf = np.vectorize(unit_cdf, otypes=[np.float])
vec_gau_cdf = np.vectorize(gau_cdf, otypes=[np.float])
vec_log_cdf = np.vectorize(log_cdf, otypes=[np.float])


	
plt.plot(x.T, err, 'o')#plotting the CDF
# plt.plot(xx,vec_unit_cdf(xx)) #plotting theoretical unit CDF
# plt.plot(xx,vec_gau_cdf(xx)) #plotting theoretical gaussian CDF
plt.plot(xx,vec_log_cdf(xx)) #plotting theoretical logarithmic CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])

#if using termux
# plt.savefig('../figs/uni_cdf.pdf')
# plt.savefig('../figs/uni_cdf.eps')
# subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window

