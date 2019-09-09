# Find S algorithm for predicting ipl player performance
# Authors : Siddharth G.C, Gautham Sivakumar, Sanka Gopi Sumanth
# Last Modified : 28/03/2018 , 4:23 PM

import csv
#Hypothesis space contains two attributes, names and cities
names= []
cities= []

#Prompt the user for choice of batsman or bowler 
type = input("Do you want to predict for a batsman or a bowler? Type 1 for batsman and 2 for bowler :")
if(type=='1'):
    temp = 'batsman'
else:
    temp = 'bowler'

#Train the model using the data from the CSV file   
with open(temp+'.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['played_well']=='yes':
            if row[temp] not in names:
                names.append(row[temp])
            if row['city'] not in cities:
                cities.append(row['city'])

#Get the test instance from the user                
name =input("Enter the name of the player:")
city=input("Enter the city:")

#If the given attribute values exist in the hypothesis space, classify as positive. Else, negative
if name in names and city in cities :
   print ("He will play well")
else:
    print ("He will not play well")
        
#EOF
