# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:44:37 2018

@author: gypjb
"""
            #PRACTICAL TWO - SHRINKING CODE
            
            
#Import the 'random' library: most useful in python for the generation of 
#random numbers
import random

#Create a list (note the [] for a list) to store sets of coordinates
#NOTE: We can add several sets of coordinates to this list, so we only
#need to run this code once 
agents = []

#Create two variable labels for the y (y0) and x (x0) coordinates  of the first
#agent, assigning them each a random value between 0 and 99
y0 = random.randint(0,99)
x0 = random.randint(0,99)

#Add the new set of coordinates for the first agent to the 'agents' list using
#the function .append()
agents.append([y0,x0])
#Inspect the agents list, showing the coordinates in format [[x,y]]
print(agents)


''' 
In the next section, we are going to work through getting rid of x0 and y0 as
objects, thus shrinking our code...
'''



#First, recreate the 'agents' list to store the more concise coordinates in 
#the future
agents = []
#Append the randomly generated y and x coordinates to the new 'agents' list
agents.append([random.randint(0,99),random.randint(0,99)])

'''
The above code basically works in the format of:
    agents.append([randomly generated y coordinate, randomly generated x
                   coordinated])
'''

#To append another set of randomly generated coordinates for a second agent,
#simply repeat the above line of code
agents.append([random.randint(0,99),random.randint(0,99)])

#We can check that two sets of coordinates have been added (one for each agent)
print(agents)

'''
The console output tells us that the above lines of code have worked:
    [[89, 48], [42, 22]] is [[y0, x0], [y1, x1]]
Thus, we have slightly reducedour code by not needing to create x0, y0 etc.,
but what we have done is make it into a stronger form for analysis

A key disadvantage to this is that we lose all sense of what the data
actually means - thus why these commented-out sections have been included.
'''


                    #ANALYSIS OF DATA

'''
In this section, an analysis will be run to calculate which agent is furthese
east, i.e. which has the largest 'x' coordinate

This is easily performed, using the built-in function max()
'''

#print the 'largest' agent
print(max(agents))

'''
The above line of code is ambiguous - max() will run through the 'agents' list
working out which is largest

Bearing in mind that our list is in the format [[0, 0], [0, 0]], max() will 
compute the largest agent to be the largest first value

Thus, if the list were [[34, 22], [24, 67]], max() would return:
    [34, 22], because the 'y' value is larger in the first set
    
With this in mind, how do we tell max() to identify the larger 'x' value 
instead - The answer is that we can pass an additional function to max()

But, to do this we will need the operator package
'''

#Import the 'operator' package: One of the most useful ways to use this 
#to call the operator.itemgetter function
import operator 


#Use the operator.itemgetter function to tell max() to compute the largest 
#agent as that with the larger x coordinate
print(max(agents, key=operator.itemgetter(1))) 

'''
The format of max()in the above code might appear confusing, lets break it 
down:
    
    * max(agents) : tells 'max' which list to run through
    * key=operator.itemgetter : is the additional function for specifiying how
        max() runs through the data
    * itemgetter(1) : tells 'max' specifically to run through the 
        x coordinates > remember that containers (y and x) are indexed
        from 0, so y ~ 0 and x ~ 1
'''


                #VISUALING THE ANALYSIS

'''
Above, we used an internal function called max, from the library operator

In this section we are going to use an external library for data visualisation
called matplotlib.pyplot
'''

#Import matplotlib.yplot library : commonly used library in python for plotting
#data on graphs 
import matplotlib.pyplot as plt

                #VISUALISING OUR AGENTS
                
#Set x and y limits of the environment (and graph)
plt.ylim(0, 99)
plt.xlim(0, 99)

#Plot the agent scatters
plt.scatter(agents[0][1],agents[0][0]) #y coordinates
plt.scatter(agents[1][1],agents[1][0]) #x coordinates

#compute and assign the agent with the larger x coordinate 
x_max = max(agents, key=operator.itemgetter(1))

#Colour the furthest east coordinate red
plt.scatter(x_max[1],x_max[0], color='red')

#Display the graph
plt.show()


