import numpy as np

#sample size
N = 10000

#randomly generate 2-tuples to simulate die throws
probarr1 = np.random.randint(1,7,size=(N,2))
problist = probarr1.tolist()

#count1 is the number of times the desired event ((2,2)) occurs
count1 = problist.count([2,2])

print("Empirical probability is",count1/N)
