# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 15:46:28 2018

@author: sgpballa
"""

                    #AGENT FRAMEWORK 
import random 

class Agent:
    def __init__(self, environment, agents):
        self.x = random.randint(0,99) #x coordinates
        self.y = random.randint(0,99) #y coordinates
        self.environment = environment
        self.agents = agents
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
        if self.store >= 3000:
            self.move = 0
        print(self.store)
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                average = (self.store + agent.store)/2
                self.store = average
                agent.store = average
                
    def distance_between(self, agents):
        return (((self.x - agents.x)**2)+((self.y - agents.y)**2))**0.5
    

            

     
          
