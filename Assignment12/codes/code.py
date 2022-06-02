import numpy as np
from math import comb

#k is what Z=X+Y maps to
#x is the pair (Xt,Yt), where Xt and Yt are instances of the binomial random variables X and Y
def ksum(x,k):
    if np.sum(x[0])+np.sum(x[1]) == k:
        return 1;
    else:
        return 0;


#Total number of trials
N = 10000

#parameters
n=5  #n for random variables X,Y
p=1/5 #p for random variables X,Y
q=1-p
k=3 #what Z=X+Y maps to

#generates N (2xn) boolean arrays, representing pairs of binomial distributions
probarr = np.random.choice([1,0],size=(N,2,n), p=[p,q])

#in-built function that generates a list of trues and falses
mapped = map(lambda x: ksum(x,k), probarr)
finarr = list(mapped) #boolean array (1-True, 0-False)

print(sum(finarr)/N) #empirical probability
print(comb(2*n,k)*(p**k)*(q**(2*n-k))) #theoretical probability
