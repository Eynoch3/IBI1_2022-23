costs=[1,8,15,7,5,14,43,40] #make a list to display data
print (str(costs[0]))
print (str(costs[1]))
print (str(costs[2]))
print (str(costs[3]))
print (str(costs[4]))
print (str(costs[5]))
print (str(costs[6]))
print (str(costs[7]))

import numpy as np
import matplotlib.pyplot as plt
N=8
scores=(1,8,15,7,5,14,43,40)
ind=np.arange(N)
width=0.7
p1=plt.bar(ind,scores,width)
plt.ylabel('socres')
plt.title('Olympic costs')
plt.xticks(ind,('Los Angeles','Seoul','Barcelona','Atlanta','Sydney','Athens','Beijing','London'))
plt.yticks(np.arange(0,60,5))
plt.show()


