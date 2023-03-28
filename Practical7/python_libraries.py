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
print (covid_data.iloc[0:1001:100,2])

print (covid_data.iloc[0:3,[0,1,3]])
my_columns = [True,True,False,True,False,False]
print (covid_data.iloc[0:3,my_columns])

print (covid_data.loc[2:4,"date"])

if 
print (covid_data.loc[,"total_cases"])
