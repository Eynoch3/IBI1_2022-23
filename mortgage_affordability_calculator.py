def mortage_affordability_calculator(x,y):
#x means the total value of the house and y means the purchaser'sannual salary
 

 if x<=y*5:
  return 'Yes'
 else:
  return'No' 

#there are two example,user can change the value to see the result
#example1
x=180000
y=25000
result1=mortage_affordability_calculator(x,y) #result=no
print (result1)
#example2
x=100000
y=40000
result2=mortage_affordability_calculator(x,y) #result=yes
print (result2)





