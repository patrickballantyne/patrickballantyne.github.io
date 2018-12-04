# Programming for Social Scientists Portfolio

This portfolio contains all work completed during the week long course in Leeds for 'Programming for Social Scientists.' 
The portfolio is to be assessed for 30% of the module mark, and the brief was:
  - The portfolio should comprise a **website** of one or more pages
  - The website should including **biographical material** explaining who you are
  - There should be some details of the **model**
  - The **code** for the model(s) should be included
  
  ---
  
## Structure of the Repository
  
  This *repository* contains all of the practical scripts and a selection of relevant outputs from each of practical sessions in Leeds.
  In this next section i will outline all the learning outcomes from each practical, before introducing the final model.
  
   NOTE: The code included for each practical section contains a significant amount of commented out ''' sections 
                of writing. The purpose of these was to assist learning of python, so that when revisiting sections of 
                code, i could understand what was going on straight away.
   
  The **SCRIPTS** are in the repository under filenames *PracticalX_TopicX.py*
  
  The **FIGURES** are in the repository under filenames *FigureX.png*
  
  ---
  
## Introduction to Agent-based modelling
  
According to Macal and North (2005, p.1), Agent-based modelling is "a modelling or computational framework for simulating dynamic  processes involving autonomous agents." In the model, a series of agents individually assess their situation in the model, and are then
able to make decisions based on that judgement (Bonabeau, 2002; Macal and North, 2005). The principle of agent-based modelling has 
been gaining significant amounts of enthusiam acorss the entire scientific community in recent years, and according Bankes (2002) it holds out the promise of a revolutionary advance in social science theory. 

Bonabeau (2002) highlighted 3 main benefits to using agent-based models over othering modelling techniques:
  
  1. Captures emergent phenomena
  2. Provides a natural description of a system
  3. Flexible in approach
  
Thus, it seems agent-based models would be a useful way of modelling say for example sheep grazing a field? This is what this portfolio
will attempt to model. Macal and North (2005) identified three requirements for a simple agent-based model, all of which will be included in this model. There will be 'Agents' in the form of numerous Sheep, there will be 'Interactions' between the sheep as they 
communicate with eachother, and an 'Environment' which is the field that the sheep wil interact with.

The following sections will outline the process by which an agent-based model of 'Sheep-Grazing' has been created.
  
  ---
  
### Practical One - Introducing Agent-Based Modelling
  
  In this practical session, the following learning outcomes were achieved:
  
   1) Created two agents, each with their own unique x and y coordinates
   2) Moved each agent according to a randomly generated number
   3) Calculated the distance between the two agents (x and y), using pythagoras' theorem
    
  The **code** for this practical session can be found at: [Script1](Practical1_ABMintro.py)
  
  As detailed in the code, there were a number of problems with the code at this point:    
  
   * Lots of repetition, when generating and moving agents
   * No behaviour other than movement, so doesn't really feel very agent-based
   * Area for agents to move about is currently infinite, which is neither practical or realistic
   * Distance calculations are very boring, when the agent starting positions are the same
    
   ---
   
### Practical Two - Shrinking Code
   
   In this practical a number of learning outcomes were achieved:
   
   1) Learned how to append the agents to a list, generating their x and y coordinates randomly this time
   2) Learned how to use the max() operation to calculate the agent with the largest x coordinate
   3) Learned how to plot our two agents using matplotlib.pyplot
    
   The **code** for this practical session can be found at: [Script2](Practical2_ShrinkingCode.py)
   
   The main outcome of this practical session was that not only was it possible to calculate the agent with the largest 'x' coordinate,
   but it was also possible to plot this calculation.
   
   The agent with the largest 'x' coordinate can be seen plotted in red in: [Figure 1](Figure1.png)
   
   ---
   
### Practical Three - Shrinking Code (Part 2)
   
   In this practical, a number of learning outcomes were achieved:
   
   1) Introduced to for-loops, used to append and create the (random) starting positions of 10 agents
   2) For-loop was used to move all agents in the list
   3) Agents were plotted using a for-loop
   4) Introduced to the concept of solving boundary effects
    
   The **code** for this section can be found at: [Script3](Practical3_ShrinkingCode2.py)
   
   It was thus possibile to use what was learned about matplotlib.pyplot to plot the ten agents, replotting each time the *move* method
   was called. 
   
   An example of this can be seen at: [Figure2](Figure2.png)
   
   At this point, the code needed to run a basic method has been significantly reduced, but there are other methods that can be 
   implemented to make our agent-based model more interesting.
   
   ---
   
### Practical Four - Building tools and functions
   
   In this practical, a number of learning outcomes were achieved: 
   
   1) A function was constructed that calculated the distance between the agents 
   2) Learned how to use time.clock() to find out how long it takes to run a length of code
    
   The **code** for this section can be found at: [Script4](Practical4_BuildingFunctions.py)
   
   ---
   
### Practical Five - Agents
   
   In this practical, a number of learning outcomes were achieved:
   
   1) A new 'Agent' class was created within a separate agentframework.py file, containing an initialiser and move method
   2) The original code to move agents based on random.random() was modified to fit within the new 'Agent' class
    
   The **code** for this section can be found at: [Script5](Practical5_Agents.py)
   
   Following creation of the 'Agent' class, the agents could be plotted: [Figure3](Figure3.png)
   
   The next steps with the ABM would be to include some more complex methods, an environment for the agents to interact with and get the    outputs to move so we can see the model working in real-time.
   
   ---

### Practical Six - Inputs and Outputs
   
   In this practical, a number of learning outcomes were achieved:
   
   1) Learned how to import the csv module, and use this to read in a in.txt file containing the 'environment'
   2) Modified the for-loop appending the agents and agentframework to the 'agents' list, to also append the 'environment'
   3) Created a new method ('eat') within the 'Agent' class to allow the agents interact with the environment
    
   The **code** for this section can be found at: [Script6](Practical6_InputsOutputs.py)
   
   An example of the agents 'eating' the environment can be seen at: [Figure4](Figure4.png)
   
   At this stage the model is really starting to take shape, however, other methods can be included, and an animation of the agents'
   methods would really help visualise the model better
   
   ---
   
### Practical Seven - Communicating
   
   In this practical, a number of learning outcomes were achieved:
   
   1) Created a 'neighbourhood' variable, which will define whether or not the agents can interact with eachother
   2) Created a new method with the 'Agent' class called 'share_with_neighbours' that allows agents to share 'food' stores with 
        eachother if the distance between eachother is less than 'neighbourhood'
   3) Learned how to use random.shuffle() to shuffle the agents list each simulation
    
   The **code** for this section can be found at: [Script7](Practical7_Communicating.py)
   
   There is no point displaying the output of this practical, since without animation the new methods do not appear clear.
   
   ---
   
### Practical Eight - Animation
   
   In this practical, a number of learning outcomes were achieved:
   
   1) Learned how to use matplotlib.animation.FuncAnimation to animate the model
   2) Learned how to implement stopping conditions into the model
   3) Learned how to enhance the visual appearance of graphs by playing with some of the extended features within matplotlib.pyplot
   
   The final model output can be seen below:
   
   


  ---
  
### References
  
* Bankes, S.C., 2002. Agent-based modeling: A revolution?. Proceedings of the National Academy of Sciences, 99(3), pp.7199-7200.

* Bonabeau, E., 2002. Agent-based modeling: Methods and techniques for simulating human systems. Proceedings of the National Academy of    Sciences, 99(suppl 3), pp.7280-7287.

* Macal, C.M. and North, M.J., 2005, December. Tutorial on agent-based modeling and simulation. In Simulation conference, 2005   proceedings of the winter (pp. 14-pp). IEEE.

  
  ---

  Return to:

## [*Homepage*](index.md)

  ---

  Go to:

### [*Education*](Education.md)  |||    [*Portfolio*](AssignmentPortfolio.md)  |||   [*Contact Details*](ContactDetails.md)

  ---
## REPOSITORY

All data, scripts and information used to create this website can be found in my [Repository](https://github.com/patrickballantyne/patrickballantyne.github.io)
