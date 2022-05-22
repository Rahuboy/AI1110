import numpy as np
from math import comb

#sample size
N = 10000

#parameters
n=10
k=6
p=1/2
q=1-p

#randomly generates N n-tuples to simulate coin tosses
#p is the probability of heads, q is the probability of tails
# 1 == heads, 0 == tails
probarr = np.random.choice([1,0],size=(N,n), p=[p,q])

#finding number of heads in each n-tuple
heads_count = np.sum(probarr, axis=1)

#finding tuples with k heads
k_heads = heads_count == k

#find tuples with last toss == heads
last_heads = probarr[:, -1] == 1
# correct_outcome = k_heads * last_heads

#generating boolean array of final result
correct_outcome = np.logical_and(k_heads, last_heads)
count = np.sum(correct_outcome)

print("Empirical Probability equals",count/N)
print("Theoretical Probability equals", comb(n-1,k-1)*(p**k)*(q**(n-k)))
