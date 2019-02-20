# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 12:40:55 2018

@author: JP
"""

import pylab as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
    
def createpitch(length, width, overlay = None):
    fig, ax = plt.subplots(1)
    #standardized values
    box = 16.5
    goal = 3.66
    gk_area = 5.5
    penalty_spot = 11
    pitch_line = 'black'
    color_overlay = 'blue'
    
    #Outer and center line
    for x in [0,length/2,length]:
        ax.plot([x,x],[0,width], pitch_line)
    for y in [0, width]:
        ax.plot([0,length],[y,y], pitch_line)
    
    #16 meter area
    for x in [box, (length-box)]:
        ax.plot([x,x],[width/2+goal+box,width/2-goal-box], pitch_line)
    for y in [width/2-goal-box, width/2+goal+box]:
        ax.plot([length-box,length],[y,y], pitch_line)
        ax.plot([0,box],[y,y], pitch_line)
    
    #5 meter area
    for x in [gk_area, (length-gk_area)]:
        ax.plot([x,x],[width/2+goal+gk_area,width/2-goal-gk_area], pitch_line)
    for y in [width/2-goal-gk_area, width/2+goal+gk_area]:
        ax.plot([length-gk_area,length],[y,y], pitch_line)
        ax.plot([0,gk_area],[y,y], pitch_line)
        
    #Circles and penalty spots.
    centre_circle = plt.Circle((length/2,width/2),9.15,color=pitch_line,fill=False)
    ax.add_patch(centre_circle)
    for spot in [penalty_spot, length/2, length-penalty_spot]:
        ax.add_patch(Circle((spot, width/2), 0.4, color = pitch_line))
    
    #Overlay over the field, if wanted.
    if overlay == 'Halfspace' or overlay == 'halfspace':
        for over_x in [box, length/2, length-box]:
            ax.plot([over_x, over_x],[0,width], linestyle='--', color=color_overlay)
        for over_x in [length/3, length-length/3]:
            ax.plot([over_x, over_x],[0, width/2-goal-box], linestyle='--', color=color_overlay)
            ax.plot([over_x, over_x],[width/2+goal+box, width], linestyle='--', color=color_overlay)
        for over_y in [width/2-goal-box, width/2-9.15,width/2+9.15, width/2+goal+box]:
            ax.plot([box, length-box],[over_y,over_y], linestyle='--', color=color_overlay)
    if overlay == 'Thirds' or overlay == 'thirds':
        for over_x in [length/3, length-length/3]:
            ax.plot([over_x, over_x],[0, width], linestyle='--', color=color_overlay)
        for over_y in [width/3, width-width/3]:
            ax.plot([0,length],[over_y,over_y], linestyle='--', color=color_overlay)
    if overlay == 'Quarters' or overlay == 'quarters':
        for over_x in [length/4, length/2, length-length/4]:
            ax.plot([over_x, over_x],[0,width], linestyle='--', color=color_overlay)
        for over_y in [width/4, width/2, width-width/4]:
            ax.plot([0,length],[over_y,over_y], linestyle='--', color=color_overlay)
    if overlay == 'Six-four' or overlay == 'six-four':
        for over_x in [length/6, length/3, length/2, length-length/3, length-length/6]:
            ax.plot([over_x, over_x],[0,width], linestyle='--', color=color_overlay)
        for over_y in [width/4, width/2, width-width/4]:
            ax.plot([0,length],[over_y,over_y], linestyle='--', color=color_overlay)
    
    # outline    
    plt.xlim((-10, length+10))
    plt.ylim((-10, width+10))
    #plt.show()
    plt.xlabel('Field length [m]')
    plt.ylabel('Field width [m]')
    return (fig, ax)

if __name__ == '__main__':
        figure = createpitch(105,68, 'halfspace')