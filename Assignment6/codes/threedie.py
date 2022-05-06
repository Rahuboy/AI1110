import numpy as np

#function that checks if the 3 tuple x satisfies the conditions of event B
def countB(x):
    if(x[2] <= 6 and x[2] >=1):
        if(x[0]==6):
            if(x[1]==5):
                return 1
    return 0


#sample size
N = 10000

#randomly generate 3-tuples to simulate die throws
probarr1 = np.random.randint(1,7,size=(N,3))
problist = probarr1.tolist()

#count1 is the number of times the desired event A intersection B occurs
count1 = problist.count([6,5,4])

#code block counts the number of times B occurs
#this value is stored in count2
bitlist = map(lambda x: countB(x), problist)
bitlist = list(bitlist)
count2 = sum(bitlist)

#output the empirical probability
print("Empirical probability is",count1/count2)
