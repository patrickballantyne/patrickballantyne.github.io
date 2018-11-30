# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 15:32:45 2018

@author: sgpballa
"""
                #PRACTICAL FIVE - AGENTS
                
'''
In this practical, we are finally going to meet some proper agents and 
convert the code we have thus far created into an object oriented version
of itself

First up, here is where our code should be:
'''

#Import the 'random' library: most useful in python for the generation of 
#random numbers
import random
#Import matplotlib.yplot library : commonly used library in python for plotting
#data on graphs
import matplotlib.pyplot

#Build a function that returns the distance between a pair of arbitrary agents
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + 
        ((agents_row_a[1] - agents_row_b[1])**2))**0.5

#Create a variable that controls how many agents we will have
num_of_agents = 10
#Create a variable that controls how many movements can occur
num_of_iterations = 100
#Create a list (note the [] for a list) to store sets of coordinates
#NOTE: We can add several sets of coordinates to this list, so we only
#need to run this code once 
agents = []

#Create a random starting position for the agents using a for-loop
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

#Set up the for-loop to move each agent in the list, implementing a torus
#to keep all agents within the environment (thus eliminating edge effects)
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

            #PLOT THE AGENTS

#Set x limits 
matplotlib.pyplot.xlim(0, 99)
#Set y limits
matplotlib.pyplot.ylim(0, 99)
#Set up a for-loop that plots all of the agents' x and y coordinates
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
#Display the output
matplotlib.pyplot.show()

#Add a for-loop that calculates the distances between the agents using the
#newly built function
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

'''
Thus, that is where our code is at so far....

Now, we are going to build ourselves an agent class:
    - It will be contained inside a new agentframework.py module
    - It will put most of the code inside the random.randint and if/else 
        statement in the above code responsible for initialising the random 
        locations and how the agents' move 
        
To start this process, we need to create a blank agentframework.py file

**We will hopefully return to this script shortly, with a new agent class**
'''
#Let's import the newly created Agent class 
#NOTE: You may need to set the working directory for this - the agentframework
#(.py) file is found in the same folder as this script for practical five
import agentframework
#Create a line of code that convinces this script that it is now connected to 
#the file agentframework.py
a=agentframework.Agent()

'''
Now that the two files are connected, let's look at initialising the agent

**We'll be doing this in the agentframework.py file**


- In the agentframework file we have made these changes:
    
    class Agent:
    def __init__(self):
       self.x(random.randint(0,99))
       self.y(random.randint(0,99))
       return

- We have defined the x and y coordinates using self.x/self.y

Let's check these changes have worked:
'''

a=agentframework.Agent()
print(a.y, a.x)

'''
The console gives an output of 
        [6 10]
Which tells us that the changes have worked 

**Returning to the framework to make a new MOVE method**
'''


            #ADDING A NEW METHOD
            
'''
In the agentframework, we have created a new method called 'move', this is 
what the code looks like currently:
    
    class Agent:
    def __init__(self):
       self.y = random.randint(0,99)
       self.x = random.randint(0,99)
       
    
    def move(self):

NOTE: The new method has not been created inside __init__ because it needs to 
        be its own method...
        
The next stage of the method is to modify this section of code that moves the
agents so that it fits with the self.x/self.y scheme inside the framework:
   
    if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 10


This is the solution, we will break it down bit by bit:
    
     if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
- Note how agents[i][0] (referring to the y coordinates) has been modified
    to fit into the self.x/self.y scheme
- Other than that, there have been no major changes to the code itself
'''

                #UPDATING THE MODEL

'''
Now, we can update our code to include the changes we have made.

This is what the code should look like now....
'''
#Import the 'random' library: most useful in python for the generation of 
#random numbers
import random
#Import matplotlib.yplot library : commonly used library in python for plotting
#data on graphs
import matplotlib.pyplot
#Import the module containing our new 'Agent' class
import agentframework

#Build a function that returns the distance between a pair of arbitrary agent
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

#Create a variable that stores our agents
num_of_agents = 10
#Create a variable that determines movements among the agents
num_of_iterations = 100
#Create a list (note the [] for a list) to store sets of coordinates
#NOTE: We can add several sets of coordinates to this list, so we only
#need to run this code once
agents = []

#Set up a for-loop that randomises the starting location of all the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

'''
This is the most significantly changed bit of code
'''

#Create a double for-loop that tells the agents to move based on the 
#randomised number system within the agentframework module
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

#Display the graph - showing movement of the Agent each time the whole code
#is re-run
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

#Add a for-loop that calculates the distances between the agents using the
#newly built function
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)