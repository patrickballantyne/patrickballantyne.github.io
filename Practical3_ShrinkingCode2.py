# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:03:32 2018

@author: gypjb
"""
                #PRACTICAL THREE - SHRINKING CODE 2
                
                
#Import the 'random' library: most useful in python for the generation of 
#random numbers
import random
#Import matplotlib.yplot library : commonly used library in python for plotting
#data on graphs
import matplotlib.pyplot as plt

#Create a list (note the [] for a list) to store sets of coordinates
#NOTE: We can add several sets of coordinates to this list, so we only
#need to run this code once 
agents = []

'''
In this next section, we are going to use for-loops to reduce the size of the 
code, and make a number of agents more flexible - this is necessary because 
how would we possibly be able to work with 1,000,000 agents?
'''

#Create a variable that controls how many agents we will have
num_of_agents = 10

'''
At the moment (In Practical 2), we have used this line of code to create
coordinates for an agents:
    
    agents.append([random.randint(0,100), random.randint(0,100)])

This line of code creates only one set of coordinates

However, if we modified this code into a for-loop, we can create as many
sets of coordinates (and thus agents) as we like...

An example of the necessary for-loop might look like this:
    for i in range(num_of_agents):
        agents.append([random.randint(0,100), random.randint(0,100)])
        
The above loop basically works through the list (num_of_agents) assigning 
coordinates to each of them
'''

        #MOVING OUR AGENTS WITH A FOR-LOOP
        
'''
The code for moving the x and y coordinates of our agents was rather
tedious, involving a great deal of repetition...

However, with a for-loop we can move our agents a specified number of times
in a shortened piece of code

NOTE: The above example of a for-loop still applies, but it is worth drawing
attention to 'for i in range(num_of_agents):
    
    i can be taken to mean each agent, where the agents are referred to as
    agents[i]
    
    Thus, with this in mind, each agents' y location is referred to as 
    agents[i][0]
'''

#Create a random starting position for the agents using a for-loop
for i in range(num_of_agents):
    agents.append([random.randint(0,100), random.randint(0,100)])
    
#Set up the for-loop to move each agent in the list of 10, twice
for i in range(num_of_agents):
    if random.random() < 0.5:
        agents[i][0] += 2
        agents[i][1] += 2
    else:
        agents[i][0] -= 2
        agents[i][1] -= 2


                    #VISUALISING CHANGES

#Set x and y limits of the environment (and graph)
plt.ylim(0, 99)
plt.xlim(0, 99)
#Plot the agents using a for-loop
for i in range(num_of_agents):
    plt.scatter(agents[i][0],agents[i][1]) 
#Display graph
plt.show()      
        
'''
Running the above lines of code repeatedly shows that the agents are moving 
according to the generation of a random number, and the for-loop which 
determines its movements   
'''    

                        #BOUNDARY EFFECTS

'''
Consider a scenario where the agents can move 100 times, they are likely to 
dissapear from our graph if the size of the graph is not managed

These are called edge effects - a major issue in geographical modelling

Our current graph only displays an area of 100x100, which is problematic
'''

                        #SOLVING BOUNDARY EFFECTS
                        
'''
There are a number of solutions:
    
    1. Infinite Plain: This works ok usually, but we will only have limited 
                        data for our environment, so eventually they will
                        wander off the edge
                        
    2. Solid Wall:     Anything trying to fall off the edge will find the edge
                        solid - however, to perform this the code itself will
                        feature a huge amount of repetition
                        
    3. Torus:           A common solution is to allow agents falling off the 
                        to come in at the bottom - to achieve this we use the 
                        modulus operator

The modulus operator (%) returns the remainder of a division, and can be used
to create a torus in a model:
    
    #This is the code
    if random.random() < 0.5:
        agents[i][0] = (agents[i][0] + 1) % 100
    else:
        agents[i][0] = (agents[i][0] - 1) % 100
        
We will implement this for loop in Practical 5
'''
