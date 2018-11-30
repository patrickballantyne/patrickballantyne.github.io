# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 13:24:20 2018

@author: gypjb
"""

                    #PRACTICAL SIX - INPUTS AND OUTPUTS
                    
'''
In this practical we are going to import some data to use as our agents' 
environment, and get the agents to interact with it

There are two steps we need to complete first:
    1) Download a text file with some comma separated values data in it - the
        file is called in.txt, download it to the same directory as this script
    2) Find the CSV reading code from the lecture notes - import the csv module
        and write some code to read in the in.txt file
'''

#IMPORTING HELPER FUNCTIONS AND GETTING THE DATA
                
#Import the csv module - this is commonly used module for the reading in and
#exporting of csv format files (typically spreadsheets and databases)                
import csv
#Import matplotlib.yplot library : commonly used library in python for plotting
#data on graphs
import matplotlib.pyplot as plt
#Import the 'random' library: most useful in python for the generation of 
#random numbers
import random
#Import the module containing our new 'Agent' class
import agentframework


#Open the csv file for this part of the practical
f = open('in.txt', newline='')

#Create a new list called 'environment,' which will be used to append the
#new csv file to this 2D list, thus creating an environment for the agents to 
#interact with
environment = []

                    #READING/APPENDING CSV FILES

#This is the code for reading in the csv file and appending it to the empty
#'environment' list
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

'''
Let's break down what th above code is doing...

 - csv.reader(f) is telling python to read in the 'in.txt' file that we have
     just handled
 - quoting=csv.QUOTE_NONNUMERIC is telling python to perform an automatic 
     conversion on the dataset, turning all unquoted fields into strings - this
     is REALLY important, because otherwise the data would be read in as 
     strings
 - rowlist = [] creates an empty list where the rows of the csv file will be 
     eventually appended to
 - rowlist.append(value) appends the values in the file to the new empty list 
     called rowlist
 - environment.append(rowlist) appends the filled in rowlist to the empty list
     created called 'environment'
'''

#Let's check we have read in the file correctly...

#NOTE: matplotlib.pyplot has been imported as 'plt,' so we can use this term 
#from now on when calling a function within matplotlib.pyplot
plt.imshow(environment)
#Display the output
plt.show()    

'''
Thus, the console has displayed an environment for us, plotted within a 300 x
300 graph

Now that we have the environment working, we are now going to get the agents to
interact with it
'''


                        #THE MODEL ITSELF
                        
'''
The overall aim of this model will be to:
    - Allow the agents to work together on the environment
    - Nibble down the environment together
    - Allow the agents to transfer resources with eachother, by providing each
        agent with the necessary information about the other agents

The rest of this practical will focus on getting the agents to have access to
the environment itself
'''

             
                    
#Create a line of code that convinces this script that it is now connected to 
#the file agentframework.py
#NOTE: how environment is in brackets after Agent - we'll return to this
a = agentframework.Agent(environment)

#Create a variable that specifies how many agents we are going to have
num_of_agents = 10
#Create a variable that specifies how many times each agent is going to move
num_of_iterations = 50
#Create an empty list for storing all the information about the agents in
agents = []

'''
We are now going to modify our original for-loop from this:
  
  
            for i in range(num_of_agents):
                agents.append(agentframework.Agent())
    
To this:
    
            for i in range(num_of_agents):
                agents.append(AgentFramework.Agent(environment))

As you can see we are going to pass the environment list into the Agent's 
constructor - to do this succesfully, we first need to adjust our Agent class
with the agentframework.py file

This is now what our Agent class looks like:
   
    class Agent:
        def __init__(self, environment):
            self.y = random.randint(0,99)
            self.x = random.randint(0,99)
            self.environment = environment
            self.store = 0

Thats it! We have set up a link inside our Agent class - as each agent changes
the environment, all the agents will link to the same environment object:
    Thus... as the environment changes for one agent, it will change for all
    
We can now add a new method to our agentframework
'''

                    #HUNGRY AGENTS

'''
As we have seen, our agent class currently looks like:
    
    import random
                 
class Agent:
    def __init__(self, environment):
       self.y = random.randint(0,99)
       self.x = random.randint(0,99)
       self.environment = environment
       self.store = 0
       
    
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100


With an initialiser (__init__), and a 'move' method

However, we are going to create a new method, which makes the agents eat away
at the environment subject to the environment not having been eaten already

This is what the new method looks like:
    
        def eat(self):
            if self.environment[self.y][self.x] > 10:
                self.environment[self.y][self.x] -= 10
                self.store += 10

In a nutshell, this method is telling python that if the environment in a 
specific place (y,x) has a value of of more than 10, then the agents will
nibble away at it, reducing its value by 10

self.store +=10 increases the 'store' of the environment within each agent, 
e.g. if you imagine each value of 10 in the environment is equivalent to some
grass, then each time they eat some grass their store of food will increase
by 10.
'''

#Append the environment to the Agents constructor
for i in range(num_of_agents):
                agents.append(agentframework.Agent(environment))

#Like we did for moving the agents, we are going to call 'eat' for each of
#the agents
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        
        
#Plot the graph to show the changes to the movement of agents and how they 
#interact with the environment
plt.xlim(0, 99)
plt.ylim(0, 99)
plt.imshow(environment)
for i in range(num_of_agents):
    plt.scatter(agents[i].x,agents[i].y)
plt.show()

'''
There we go... we have the agents interacting with the environment...

There are a number of further activities we could do to develop our model 
further - SEE THE PRACTICAL HANDOUT FOR SOME OF THESE

'''
