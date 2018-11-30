# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:12:34 2018

@author: gypjb
"""

                #PRACTICAL 4 - BUILDING FUNCTIONS

#Import the 'random' library: most useful in python for the generation of 
#random numbers
import random
#Import matplotlib.yplot library : commonly used library in python for plotting
#data on graphs
import matplotlib.pyplot
#Useful for calculating time taken to run certain lines of code - most useful
#function is time.clock()
import time 

'''
When calculating the distances between agents in the model, we used this 
line of code:
    
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - 
          agents[1][1])**2))**0.5

print(answer)

Ideally, we want this line of code to work for any specified pair of agents: 
    Ultimately passing every pair through this to see how far apart they
    are...
    
In order to do this, we need to turn this line of code into a function that 
will itself work out the distance between each pair of agents...
'''

                    #BUILDING A FUNCTION

'''
In this section we are going to start building a function that works out the
distance between each of the agents in the model

Lets look at the first sentence:
def distance_between(agents_row_a, agents_row_b):
    

The above line of code does a number of things:
    1. Defines the new function, calling it distance_between
    2. Takes in two arbitrary agents - at the moment two rows in our agents 
        list
        
Thus, we will be able to use it when it's completed to make distance 
calculations like this for example:
    
    distance = distance_between(agents[0], agents[1])
    print(distance)
'''

                    #SLEIGHT OF HAND
                    
''' 
You might notice that in the line of code:
        'def distance_between(agents_row_a, agents_row_b)'

We have started referring to the agents as rows, and not something like 
agent[0]...

Now, what we are doing is referring to agents[0] as agents_row_a..

This means that before where we would obtain the y value of an agent as
agent[0][0], we would now refer to it as agents_row_a[0]
'''


                    #THE FUNCTION

#Build a function that returns the distance between a pair of arbitrary agents
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0]-agents_row_b[0])**2)+((agents_row_a[1]-
            agents_row_b[1])**2))**0.5                    


'''
Ok, lets breakdown what this line of code is actually doing

- def distance_between(agents_row_a, agents_row_b):
    
        As we have already mentioned, this line of code defines the new 
        function and takes in two rows in our agents list

- return ((agents_row_a[0]-agents_row_b[0])**2):
    
        This line of code is the first section of the pythagoras equation, 
        which is working out the distance between the y coordinates of two
        different agents (agents_row_a & agents_row_b)
        
        It then squares them to fulfill the equation

- ((agents_row_a[1]-agents_row_b[1])**2)):
        
        This is the second part of the equation, which works out the distance
        between the x coordinates of the two different agents 
        
- **0.5:
    
        The whole equation is then square rooted, to work out the euclidean 
        distance between both of the agents

'''

                    #TIME CONSTRAINTS
                    
'''
When this model is finished, when it tests each combination of agent pairs
against eachother, this is quite an aggressive piece of code 

Thus, it is important to know how long the job will take to run

Let's see how to do this
'''
#This effectively starts the digital stopwatch 
start = time.clock()

'''
The section of code you want to time would then go in here
'''

#This effectively ends the digital stopwatch 
end = time.clock()

#We can then find out how long it took to run a length of code
print("time = " + str(end - start))
