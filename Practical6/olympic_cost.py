costs=[1,8,15,7,5,14,43,40] #make a list to display data
sorted_values=sorted(costs) #print the data
print(sorted_values)

import numpy as np 
import matplotlib.pyplot as plt #create a bar chart
N=8 #there are 8 pieces of data
scores=sorted_values #enter 8 specific data
ind=np.arange(N) #the x locations for the groups
width=0.7 #the width of the bar
p1=plt.bar(ind,scores,width) #related properties of a graph
plt.ylabel('socres') #name for the x axis
plt.title('Olympic costs') #name for the y axis  
plt.xticks(ind,('Los Angeles','Seoul','Barcelona','Atlanta','Sydney','Athens','Beijing','London')) #each label name for the x axis
plt.yticks(np.arange(0,60,5)) #the start value ,the end value and the unit distance of the y axis
plt.show() #display image


