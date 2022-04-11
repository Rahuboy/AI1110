# ICSE 2018 Grade 12 17(a)
# Rahul Ramachandran (cs21btech11049)

# On plugging the vector for the line vector in the equation for the parabola, we get the 
# characteristic equation kappa^2 - 16 . Solving this gives us lambda and the points.

import numpy as np

charpol = [1,0,-16] #characteristic polynomial

rts = np.roots(charpol) #roots

#using the equation of the line
point1 = np.array([2,0])+rts[0]*np.array([0,1]) 
point2 = np.array([2,0])+rts[1]*np.array([0,1])

print("The first point is ({},{})".format(point1[0],point1[1]))
print("The second point is ({},{})".format(point2[0],point2[1]))