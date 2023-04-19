movie_genre={'Comedy':73, 'Action':42, 'Romance':38, 'Fantasy':28, 'Science-fiction':22, 'Horror':19, 'Crime':18, 'Documentary':12, 'History':8, 'War':7} # crate and print a dictionary to record the data


import matplotlib.pyplot as plt #draw a pie chart
labels = list(movie_genre.keys()) #enter all movie types as data tags
sizes = list(movie_genre.values()) #enter all the data
explode = (0,0,0,0,0.1,0,0,0,0,0) #set the highlight module offset
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',
        shadow=False, startangle=90) #set the pie properties and draw the image
plt.axis('equal') #display images
plt.show() #save and display

a='Comedy' # create a variable of the requested genre that can be modified.
print (movie_genre[a]) #print the value

