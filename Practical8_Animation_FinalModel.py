# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:36:02 2018

@author: sgpballa
"""
                #PRACTICAL 8 - ANIMATION AND FINAL MODEL


#IMPORT LIBRARIES
import random #Used to generate random numbers
import csv #Used to reading in csv files
import matplotlib.pyplot #Used for plotting outputs
import matplotlib.animation #Used to animating outputs
import agentframework #Contains the newly created 'Agent' class

#SET UP THE VARIABLES
num_of_agents = 25 #Define how many agents the model will have
num_of_iterations = 100 #Define how many movements will form one simulation
neighbourhood = 5 #Define the minimum distance for interaction between agents
#Create a list to store all of our agents in
agents = [] #Create an empty list to store the agents in 
environment = [] #Create another empty list to store the environment in


#SETTING UP THE MODEL
#Connect the model script to our agentframework.py file
a = agentframework.Agent(environment,agents) 

#READING IN THE ENVIRONMENT
f = open('in.txt', newline='') #Open the 'environment' csv file
#Read in the csv file and append it to the 'environment' list
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) 
for row in reader:
    rowlist = []
    for value in row:				
        rowlist.append(value)
    environment.append(rowlist)
#Close the file
f.close() 

#Loop through and append the 25 Agents into the 'agents' list
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

#SET UP THE MODEL VISUALISATION
#Define the figure size for the model visualisation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
#Draw axes onto the model visualisation
ax = fig.add_axes([0, 0, 1, 1])

'''
At this point, it needs to be demonstrated that a stopping condition has 
been introduced into the Agent class itself.

Within the 'eat' method, the following code was added

#ORIGINAL CODE
            def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
#NEW CODE
        if self.store >= 3000:
            self.move = 0
        print(self.store) #Used to check the model stops at 3000

This stops the model if any one of the sheep has eaten more than 3000 of the
environment
'''

#Define the update function to animate the model, allowing agents to move, eat
#and share with neighbours *subject to conditions*
def update(frame_number):
    global carry_on

#NOTE: The starting positions of the Agents have not been randomised each 
#iteration so as to create a more realistic model of 'sheep grazing'    
    fig.clear()  
    matplotlib.pyplot.imshow(environment) #Display the environment
    #Loop through the agents so that they perform various methods, including
    #the new 'stuffed' method, which determines the stopping point of the model
    for i in range(num_of_agents): 
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
            
#MODEL VISUALISATION
#Scatter plot all of the agents onto a figure, with chosen design preferences
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color="white",
                                  edgecolor="black", marker='o', s=50)
    #Set up the figure limits
    matplotlib.pyplot.ylim(0,100)
    matplotlib.pyplot.xlim(0,100)
    matplotlib.pyplot.title("Final Model")
    matplotlib.pyplot.legend(["Sheep"], loc = "upper center")
    matplotlib.pyplot.ylabel("Environment ('Grazing Field')")
    matplotlib.pyplot.xlabel("Environment ('Grazing Field')")

#MODEL ANIMATION
#Animate the model, so it runs until the stopping condition in the 'stuffed'
#method is reached
animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False)
#Display final model visualisation
matplotlib.pyplot.show()
#Save figure - NOTE: Need to set working directory to desired area
animation.save("final_model_output.gif", writer = "imagemagick")
    
