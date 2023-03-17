n=2 #start with two habbit
gener=1 #first generation
while n<=100: #find the first generation when more than 100 rabbits have been born
  n=n*2 #each pair can produce two new rabbits
  gener=gener+1
print ("Starting at the"+str(gener)+" generation, over 100 rabbits have been born")

