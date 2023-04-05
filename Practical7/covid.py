import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/cygwin64/home/86188/IBI1_2022-23/IBI1_2022-23/Practical7")

print (os.getcwd())
print (os.listdir())

covid_data = pd.read_csv("full_data.csv")
print (covid_data.head(5)) # it shows the first five lines of data in the file
print (covid_data.info())
print (covid_data.describe()) #the mean of the new cases is 194.546733
                              #the standard deviation is 2083.395028
                              #the range of total cases is from 0.00 to 777798.00
print (covid_data.iloc[0,1]) #the data in the first row and second column
print (covid_data.iloc[2,0:5]) #the data in the third row and the column from first to fifth
print (covid_data.iloc[0:2,:]) #the data in the row from first to second and show all the columns 
print (covid_data.iloc[0:10:2,0:5]) #the data from first row to tenth, take it every two row,the column from fisrt to fifth
print (covid_data.iloc[999:2001:100,2])

print (covid_data.iloc[0:3,[0,1,3]])
my_columns = [True,True,False,True,False,False]
print (covid_data.iloc[0:3,my_columns])

print (covid_data.loc[2:4,"date"])



print (covid_data.loc[covid_data.loc[:,"location"]=="Afghanistan","total_cases"])
print (covid_data.loc[0:81,"total_cases"])

my_columns=[False,True,True,True,False,False]
new_data=covid_data.loc[covid_data.loc[:,'date']=='2020-03-31',my_columns]
print (new_data)
a=new_data.iloc[:,1:3]
print (np.mean(a))

import matplotlib.pyplot as plt
new_data_new_cases=new_data.loc[:,"new_cases"]
fig=plt.figure()
view=plt.boxplot(new_data_new_cases)
plt.show()

import matplotlib.pyplot as plt
new_data_new_deaths=new_data.loc[:,"new_deaths"]
fig=plt.figure()
view=plt.boxplot(new_data_new_deaths)
plt.show()

world_dates=covid_data.loc[covid_data.loc[:,"location"]=="World","date"]
world_new_cases=covid_data.loc[covid_data.loc[:,"location"]=='World','new_cases']
world_new_deaths=covid_data.loc[covid_data.loc[:,"location"]=='World','new_deaths']
plt.plot(world_dates, world_new_cases,'ro')
plt.plot(world_dates, world_new_deaths,'bo')
plt.ylabel('new cases/deaths')
plt.title('new cases and new deaths across the world')
plt.xlabel("dates")
plt.show()

China_dates=covid_data.loc[covid_data.loc[:,'location']=='China','date']
China_total_cases=covid_data.loc[covid_data.loc[:,'location']=='China','total_cases']
China_total_deaths=covid_data.loc[covid_data.loc[:,'location']=='China','total_deaths']
plt.plot(China_dates, China_total_cases,'ro')
plt.plot(China_dates, China_total_deaths,'bo')
plt.xlabel("dates")
plt.ylabel('total cases/deaths')
plt.title("total cases and deaths in China")
plt.show()



