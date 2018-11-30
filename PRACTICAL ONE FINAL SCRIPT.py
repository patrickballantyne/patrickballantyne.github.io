# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:58:17 2018

@author: gypjb
"""
                    #PRACTICAL ONE - INTRO TO AGENT-BASED MODELS


#Create two variable labels for the y (y0) and x (x0) coordinates  of the first
#agent, assigning them each values of 50

y0 = 50 
x0 = 50

#Import the 'random' library: most useful in python for the generation of 
#random numbers
import random

                #FIRST AGENT 

random_number = random.random() #generates a random floating point number b
#between 0 and juts less than one

#Create a control-flow statement to move our first agent one step according
#to the generation of a random number


                #Y COORDINATE
if random_number < 0.5: #move the y coordinate according to the random number
   y0 += 1 #y0 increases by 1 if random number is less than 0.5
else:
   y0 -= 1 #y0 decreases by 1 if random number is not less than 0.5 
#Inspect how y0 has changed
print(y0)

                #X COORDINATE
if random_number < 0.5: #move the x coordinate according to the random number
    x0 += 1 #x0 increases by 1 if random number is less than 0.5
else:
    x0 -= 1 #x0 decreases by 1 if random number is not less than 0.5 
#Inspect how x0 has changed
print(x0)

#We can then make our first agent move again (x and y) by just copying the
#above code again:

                #Y COORDINATE
if random_number < 0.5: #move the y coordinate according to the random number
   y0 += 1 #y0 increases by 1 if random number is less than 0.5
else:
   y0 -= 1 #y0 decreases by 1 if random number is not less than 0.5 
#Inspect how y0 has changed
print(y0)

                #X COORDINATE
if random_number < 0.5: #move the x coordinate according to the random number
    x0 += 1 #x0 increases by 1 if random number is less than 0.5
else:
    x0 -= 1 #x0 decreases by 1 if random number is not less than 0.5 
#Inspect how x0 has changed
print(x0)



                #SECOND AGENT
'''In this next section, we are going to add in a second agent to do the same
#as the first agent'''
                
#Create two variable labels for the y (y0) and x (x0) coordinates  of the 
#second agent, assigning them each values of 50
y1 = 50 
x1 = 50

random_number = random.random() #generates a random floating point number b
#between 0 and juts less than one

#Create a control-flow statement to move our first agent one step according
#to the generation of a random number


                #Y COORDINATE
if random_number < 0.5: #move the y coordinate according to the random number
   y1 += 1 #y0 increases by 1 if random number is less than 0.5
else:
   y1 -= 1 #y0 decreases by 1 if random number is not less than 0.5 
#Inspect how y0 has changed
print(y1)

                #X COORDINATE
if random_number < 0.5: #move the x coordinate according to the random number
    x1 += 1 #x0 increases by 1 if random number is less than 0.5
else:
    x1 -= 1 #x0 decreases by 1 if random number is not less than 0.5 
#Inspect how x0 has changed
print(x1)

#We can then make our first agent move again (x and y) by just copying the
#above code again:

                #Y COORDINATE
if random_number < 0.5: #move the y coordinate according to the random number
   y1 += 1 #y0 increases by 1 if random number is less than 0.5
else:
   y1 -= 1 #y0 decreases by 1 if random number is not less than 0.5 
#Inspect how y0 has changed
print(y1)

                #X COORDINATE
if random_number < 0.5: #move the x coordinate according to the random number
    x1 += 1 #x0 increases by 1 if random number is less than 0.5
else:
    x1 -= 1 #x0 decreases by 1 if random number is not less than 0.5 
#Inspect how x0 has changed
print(x1)


                #DISTANCE BETWEEN AGENTS

'''In this next section, we are going to add some code to work out the distance
#between the two agents we have just created - this is key in an ABM as agents
#need to know who is near them, so they can decide whether or not to interact
#with them
                
#To work out the straight-line (Euclidean) distance between two agents we need
#to use pythagoras' theorem

#Calculate the euclidean distance between the two agents using the following
#formula
                
 answer = (((distance between y coordinates)squared)+ ((distance between 
                x coordinates)squared)) square-rooted '''
    
dist = (((y0-y1)**2)+(x0-x1)**2)**0.5 #calculate the euclidean distance
print(dist) #print the result

'''
At the moment, it is quite difficult to check the result because we don't 
know what x and y values are being generated

However, if we set the values to something we know and then re-run the 
calculation, we can check the answer:

y0 = 0
x0 = 0
y1 = 4
x1 = 3

dist = (((y0-y1)**2)+(x0-x1)**2)**0.5 #calculate the euclidean distance
print(dist) #print the result

Thus, we have checked the formula is working correctly because it has given 
us the correct answer ~ 5.0 '''


                #PROBLEMS
                
''' At the moment, the code above has some issues:
    - Lots of repetition
    - Doesn't feel very agent based , there is no behaviour other than 
      movement, which is entirely dependent on fixed values (Markovian)
    - The area is currently infinite in size
    - Having the same start point makes for very boring distances

In the next practical, we will start to correct some of these issues
'''


