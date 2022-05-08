import numpy as np

#Let 1 represent a white ball and 0 represent a black ball

#When no ball has been drawn
urn1 = np.array([1]*5 + [0]*10)

#When a black ball has been drawn
urn2 = np.array([1]*5 + [0]*9)

#Sample size
N=5000

#Draw the first ball
draw1 = np.random.choice(urn1, size=N)
unique1, count1 = np.unique(draw1, return_counts=True)
bitarray1 = dict(zip(unique1, count1))

#Draw the second ball (given that the first is black)
draw2 = np.random.choice(urn2, size=bitarray1[0])
unique2, count2 = np.unique(draw2, return_counts=True)
bitarray2 = dict(zip(unique2, count2))

print("Empirical probability of 2 black balls being drawn is",bitarray2[0]/N)
