# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 18:45:27 2018

@author: JP
"""
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

print(str("What are the length (goal to goal), width, and unity (meters/yards) of the field?"))
print(str("For example you type: CreatePitch(105,68, 'meters') with unity between single quotation marks."))
print(str("Now you can try:"))
   
def CreatePitch(length, width, unity): # in meters
    """
    creates a plot in which the 'length' is the length of the pitch (goal to goal).
    And 'width' is the width of the pitch (sideline to sideline). 
    Fill in the unity in meters or in yards.

    """
    #Set unity
    if unity == "meters":
        # Set boundaries
        if length >= 120.5 or width >= 75.5:
            return(str("Field dimensions are too big for meters as unity, didn't you mean yards as unity?\
                       Otherwise the maximum length is 120 meters and the maximum width is 75 meters. Please try again"))
        #Run program if unity and boundaries are accepted
        else:
            #Create figure
            fig=plt.figure()
            #fig.set_size_inches(7, 5)
            ax=fig.add_subplot(1,1,1)
           
            #Pitch Outline & Centre Line
            plt.plot([0,0],[0,width], color="black")
            plt.plot([0,length],[width,width], color="black")
            plt.plot([length,length],[width,0], color="black")
            plt.plot([length,0],[0,0], color="black")
            plt.plot([length/2,length/2],[0,width], color="black")
            
            #Left Penalty Area
            plt.plot([16.5 ,16.5],[(width/2 +16.5),(width/2-16.5)],color="black")
            plt.plot([0,16.5],[(width/2 +16.5),(width/2 +16.5)],color="black")
            plt.plot([16.5,0],[(width/2 -16.5),(width/2 -16.5)],color="black")
            
            #Right Penalty Area
            plt.plot([(length-16.5),length],[(width/2 +16.5),(width/2 +16.5)],color="black")
            plt.plot([(length-16.5), (length-16.5)],[(width/2 +16.5),(width/2-16.5)],color="black")
            plt.plot([(length-16.5),length],[(width/2 -16.5),(width/2 -16.5)],color="black")
            
            #Left 5-meters Box
            plt.plot([0,5.5],[(width/2+7.32/2+5.5),(width/2+7.32/2+5.5)],color="black")
            plt.plot([5.5,5.5],[(width/2+7.32/2+5.5),(width/2-7.32/2-5.5)],color="black")
            plt.plot([5.5,0.5],[(width/2-7.32/2-5.5),(width/2-7.32/2-5.5)],color="black")
            
            #Right 5 -meters Box
            plt.plot([length,length-5.5],[(width/2+7.32/2+5.5),(width/2+7.32/2+5.5)],color="black")
            plt.plot([length-5.5,length-5.5],[(width/2+7.32/2+5.5),width/2-7.32/2-5.5],color="black")
            plt.plot([length-5.5,length],[width/2-7.32/2-5.5,width/2-7.32/2-5.5],color="black")
            
            #Prepare Circles
            centreCircle = plt.Circle((length/2,width/2),9.15,color="black",fill=False)
            centreSpot = plt.Circle((length/2,width/2),0.8,color="black")
            leftPenSpot = plt.Circle((11,width/2),0.8,color="black")
            rightPenSpot = plt.Circle((length-11,width/2),0.8,color="black")
            
            #Draw Circles
            ax.add_patch(centreCircle)
            ax.add_patch(centreSpot)
            ax.add_patch(leftPenSpot)
            ax.add_patch(rightPenSpot)
            
            #Prepare Arcs
            leftArc = Arc((11,width/2),height=18.3,width=18.3,angle=0,theta1=308,theta2=52,color="black")
            rightArc = Arc((length-11,width/2),height=18.3,width=18.3,angle=0,theta1=128,theta2=232,color="black")
            
            #Draw Arcs
            ax.add_patch(leftArc)
            ax.add_patch(rightArc)
            #Axis titles
            plt.xlabel('Field length [m]')
            plt.ylabel('Field width [m]')
    #check unity again
    elif unity == "yards":
        #check boundaries again
        if width <= 95:
            return(str("Didn't you mean meters as unity?"))
        elif length >= 131 or width >= 101:
            return(str("Field dimensions are too big. Maximum length is 130, maximum width is 100"))
        #Run program if unity and boundaries are accepted
        else:
            #Create figure
            fig=plt.figure()
            #fig.set_size_inches(7, 5)
            ax=fig.add_subplot(1,1,1)
           
            #Pitch Outline & Centre Line
            plt.plot([0,0],[0,width], color="black")
            plt.plot([0,length],[width,width], color="black")
            plt.plot([length,length],[width,0], color="black")
            plt.plot([length,0],[0,0], color="black")
            plt.plot([length/2,length/2],[0,width], color="black")
            
            #Left Penalty Area
            plt.plot([18 ,18],[(width/2 +18),(width/2-18)],color="black")
            plt.plot([0,18],[(width/2 +18),(width/2 +18)],color="black")
            plt.plot([18,0],[(width/2 -18),(width/2 -18)],color="black")
            
            #Right Penalty Area
            plt.plot([(length-18),length],[(width/2 +18),(width/2 +18)],color="black")
            plt.plot([(length-18), (length-18)],[(width/2 +18),(width/2-18)],color="black")
            plt.plot([(length-18),length],[(width/2 -18),(width/2 -18)],color="black")
            
            #Left 6-yard Box
            plt.plot([0,6],[(width/2+7.32/2+6),(width/2+7.32/2+6)],color="black")
            plt.plot([6,6],[(width/2+7.32/2+6),(width/2-7.32/2-6)],color="black")
            plt.plot([6,0],[(width/2-7.32/2-6),(width/2-7.32/2-6)],color="black")
            
            #Right 6-yard Box
            plt.plot([length,length-6],[(width/2+7.32/2+6),(width/2+7.32/2+6)],color="black")
            plt.plot([length-6,length-6],[(width/2+7.32/2+6),width/2-7.32/2-6],color="black")
            plt.plot([length-6,length],[(width/2-7.32/2-6),width/2-7.32/2-6],color="black")
            
            #Prepare Circles; 10 yards distance. penalty on 12 yards
            centreCircle = plt.Circle((length/2,width/2),10,color="black",fill=False)
            centreSpot = plt.Circle((length/2,width/2),0.8,color="black")
            leftPenSpot = plt.Circle((12,width/2),0.8,color="black")
            rightPenSpot = plt.Circle((length-12,width/2),0.8,color="black")
            
            #Draw Circles
            ax.add_patch(centreCircle)
            ax.add_patch(centreSpot)
            ax.add_patch(leftPenSpot)
            ax.add_patch(rightPenSpot)
            
            #Prepare Arcs
            leftArc = Arc((11,width/2),height=20,width=20,angle=0,theta1=312,theta2=48,color="black")
            rightArc = Arc((length-11,width/2),height=20,width=20,angle=0,theta1=130,theta2=230,color="black")
            
            #Draw Arcs
            ax.add_patch(leftArc)
            ax.add_patch(rightArc)
            
            #Axis titles
            plt.xlabel('Field length [yards]')
            plt.ylabel('Field widt [yards]')
    else:
        print()
        print(str("Input was not correct for unity. Either use 'meters' or 'yards'. All lower-case letters"))
        print(str("Please retry the CreatePitch function, with the right unity"))
