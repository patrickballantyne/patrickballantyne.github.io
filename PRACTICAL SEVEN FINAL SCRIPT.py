# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:05:22 2018

@author: gypjb
"""
            #PRACTICAL 7 - COMMUNICATING
            
'''
In this practical we are going to get our agents to talk to eachother, by
altering eachother's variable

There are a number of steps to this:
    1. The agents first need to know about eachother
    2. The agents need to be able to check their neighborhood
    3. The agents need to be able to scan the list of other agents, altering 
        their variables and their neighbours variables to transfer information
        to eachother
'''

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
#Create a variable that specifies how many agents we are going to have
num_of_agents = 100
#Create a variable that specifies how many times each agent is going to move
num_of_iterations = 10
#Create an empty list for storing all the information about the agents in
agents = []
#Create a new variable called neighbourhood 
neighbourhood = 20

'''
NORMALLY, we would have all of our model parameters at the top of the model - 
e.g. num_of_agents, agents = []. 
This is good practice within python... however, for the purpose of these
practical for now we will keep it in this format

'''

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
Now we are going to focus on the first activity in this practical, getting
the agents to know about eachother
'''

#Create a line of code that convinces this script that it is now connected to 
#the file agentframework.py
#NOTE: now we have environment, agents in brackets
    #This is the step taken to get a list of the agents into each agent
a = agentframework.Agent(environment, agents)

#Loop through and create the agents, appending information from the agent
#framework, including information on the surrounding environment, and a 
#list of the other agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    
'''
Now we aregoing to start constructing another behavioural method for our agents
Currently, we have 'move' and 'eat'

In this section, we are going to create a method called 'share with neighbours'
Which does two things:
    1. Searches for close neighbours
    2. Shares resources with neighbours 
'''

#Adjust the agents loop to include the new sharing with neighbours method
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

'''
We now need to build this method in the agentframework....

Here is the basic algorithm for it

# Loop through the agents in self.agents .
    # Calculate the distance between self and the current other agent:
    distance = self.distance_between(agent) 
    # If distance is less than or equal to the neighbourhood
        # Sum self.store and agent.store .
        # Divide sum by two to calculate average.
        # self.store = average
            # agent.store = average
    # End if
# End loop
    
    Thus... the final method in the agentframework looks like this:
        
        def share_with_neighbours(self, neighbourhood):
            for agent in self.agents:
                dist = self.distance_between(agent)
                if dist <= neighbourhood:
                    average = (self.store + agent.store)/2
                    self.store = average
                    agent.store = average
'''

                #SHARE WITH NEIGHBOURS

'''
It makes sense to break down the method, to make sense of whats goin on

 - for agent in self.agents: *Loops through the agents list*
 - dist = self.distance_between(agent) *Calculates the distance between self
     and current other agents
 - if dist <= neighborhood *works out whether the self agent is within 20 of
     a nearby agent
 - average = (self.store + agent.store)/2 *calculates the average store between
     the self agent and the other agents
- self.store/agent.store = average *sets the food store for self and the agent
     as the average value of the two (sharing)

    
HOWEVER, you will notice a field in the method called distance_between which 
we have not touched upon for a while

In the agentframework we also have to create a new method call for
distance_between, this is what it looks like:
    
    def distance_between(self,agent):
        return (((self.x - agent.x)**2)+((self.y - agent.y)**2))**0.5
        
Now, this is a relatively simple bit of code, applying the previously used
pythagoras' theorem to calculate the (euclidean distance) between the x and y 
coordinates of 'self' and the other agents
'''

                    #AGENT FRAMEWORK
                    
'''
Thus, now that we have included two new method calls in our new Agent class,
our agentframework at this point looks like:
    
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
            
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
              dist = self.distance_between(agent)
              if dist <= neighbourhood:
                average = (self.store + agent.store)/2
                self.store = average
                agent.store = average
                
    def distance_between(self,agent):
        return (((self.x - agent.x)**2)+((self.y - agent.y)**2))**0.5
        
'''


                #MODEL ARTEFACTS
                
'''
A model artefact is a pattern/error that emerges from the model because of the
way it works as a model, not how it replicates reality....

Our model typically deploys left-to-right top-to-bottom scanning, which results
in a common artefact...

Because of this, is it common to randomise the order in which agents are 
processed each iteration, otherwise the first agent will likely accumulate 
significantly more wealth(food in this case) than the other agents in the list

Lets shuffle the order of agents

You'll remember earlier we used this function to loop through the agents 
telling them to execute certain methods:
'''
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

#MODIFY THE ABOVE LOOP TO SHUFFLE THE AGENTS LIST
        for j in range(num_of_iterations):
            random.shuffle(agents) 
            for i in range(num_of_agents):
                agents[i].move()
                agents[i].eat()
                agents[i].share_with_neighbours(neighbourhood)


