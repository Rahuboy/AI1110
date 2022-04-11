# ICSE 2018 Grade 12 17(a)
# Rahul Ramachandran (cs21btech11049)

# This code plots the parabola y^2 = 8x and the line x=2, and the intersection points that 
# were verified in points.py. It also shades the enclosed region.


import matplotlib.pyplot as plt
import numpy as np

def f(y,a):
    return y**2/a



fylist = np.linspace(-6,6,num=500)
fxlist = f(fylist,8)

xaxisx = [-1,8]
xaxisy = [0,0]

yaxisx = [0,0]
yaxisy = [-7,7]

gx = [2,2]
gy = [-7,7]

xpoints = [2,2,2]
ypoints = [4,-4,0]

plt.plot(fxlist, fylist, color = "b", label = "$y^2 = 8x$")
plt.plot(xaxisx, xaxisy, color = "k")
plt.plot(yaxisx, yaxisy, color = "k")
plt.plot(gx, gy, color = "r", label = "$x = 2$")
plt.scatter(xpoints,ypoints, s=20)

plt.text(2.1,3.6,"(2,4)")
plt.text(2.1,-0.6,"(2,0)")
plt.text(2.1,-3.8,"(2,-4)")

plt.fill_between(np.linspace(0, 2, num=500),np.sqrt(np.linspace(0, 2, num=500)*8), alpha=0.25, color = "#00FFBF", )
plt.fill_between(np.linspace(0, 2, num=500),-np.sqrt(np.linspace(0, 2, num=500)*8), alpha = 0.25, color="#00FFBF")

plt.legend(loc="best")

plt.show()
