#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 16:58:18 2022

@author: ollywhaites
"""

"""
import functions used
"""

import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['hatch.linewidth'] = 1.0 
mpl.rcParams['font.family'] = 'Avenir'

"""
functions
"""

def params():
    """
    
    Returns the default parameters for plots.
    
    Parameters
    -----------

    
    Returns
    -----------
    
    params: dictionary of parameters required for plots
    
    """

    params = {}
    # model parameters
    params['colors'] =  {'backgroundColor': 'white',
                            'backgroundColor_alt':'gray',
                            'textColor':'black',
                            'lineColor1':'white',
                            'lineColor1_alt':'blue',
                            'lineColor2':'white',
                            'lineColor2_alt':'black',
                            'lineColor3':'red',
                            'lineColor3_alt':'blue'}

    return params



def radar(data,Attributes,players,colors_ticks = None,params = params(),save = False, Dir = ''):
    """
    
    A program designed to plot the radar of up to two players against the average.
    
    Parameters
    -----------
                data: dataframe of the players data. Must have columns that 
                        are present in Attributes list
                Attributes: list of attributes or stats for theta axis plot
                players: list of up to two player names that are within the 
                        data dataframe variable.
                colors_ticks: color scheme of each individual attribute label 
                            on plot. Default = None which leads to text color
                            ticks.
                params: dict of parameters used in the plot process
    
    Returns
    -----------
                fig: matplotlib figure object of radar
                ax: matplotlib ax object of figure

    
    """
    
    #retrieve colors from parameters variable
    colors = params['colors']    

    #get the number of ticks
    AttNo = len(Attributes)
    
    
    #set the default colours if not given
    if colors_ticks == None:
        colors_ticks = [colors['textColor']]*AttNo
    
    
    #normalise and shift data
    data_norm=(data-data.min())/(data.max()-data.min())
    
    
    #construct the angles for which the ticks will be placed on the radar
    angles = [(n/float(AttNo))*2*np.pi for n in range(AttNo)]
    angles += angles [:1]
    
    #construct figure
    fig = plt.figure(figsize = [10,10],dpi = 100);
    
    '''
    title
    '''
    fig.text(0.05,0.95,'Defensive, ',
              color = 'darkred',
              fontsize = 18,
              ha = 'left')
    fig.text(0.18, 0.95, 'Possession ',
              color = 'darkorange',
              fontsize = 18,
              ha = 'left')
    fig.text(0.32,0.95, 'and',
              color = 'black',
              fontsize = 18,
              ha = 'left')
    fig.text(0.37,0.95,'Final Product',
              color = 'darkblue',
              fontsize = 18,
              ha = 'left')
    fig.text(0.53,0.95,'statistics for {}'.format(players[1]),
              color = 'black',
              fontsize = 18,
              ha = 'left')
    
    fig.text(0.05,0.1,'*% is accuracy of pass.',
              color = 'gray',
              fontsize = 12,
              ha = 'left')
    fig.text(0.05,0.075,'*All other stats are p90.',
              color = 'gray',
              fontsize = 12,
              ha = 'left')

     
    '''
    axis created
    '''
    ax = fig.add_subplot(1,1,1,polar = True);
    
    
    fig.set_facecolor(colors['backgroundColor'])
    ax.patch.set_facecolor(colors['backgroundColor'])
    
    
    ax.grid(ls = '--')
    
    ax.set_ylim([0,1])
    
       
    '''
    format grid style
    '''
    #Add the attribute labels to our axes
    plt.xticks(angles[:-1],Attributes)

    
    yticks, _ = plt.yticks()
    
    #set alternating background for style
    for i in range(len(yticks) - 3):
    
        ax.fill_between(np.linspace(0, 2*np.pi, 100), yticks[2*i], yticks[2*i + 1],
                        alpha = 0.1,
                        color=colors['backgroundColor_alt'],
                        zorder=0)
    ax.set_yticklabels([''])
    plt.xticks(color = colors['textColor'])
    
    #initialise ticks
    yticks,_ = plt.yticks();
    
    
    '''
    add tick labels to theta axis
    '''
    
    labels = []
    for label, angle, color_tick in zip(ax.get_xticklabels(), angles,colors_ticks):
        x,y = label.get_position()
        lab = ax.text(x,y, label.get_text(), transform=label.get_transform(),
                      ha=label.get_ha(), va=label.get_va(),
                      color = color_tick,
                      fontsize = 10)
        
        #change rotation for different positions so that labels aren't upside down
        if angle*180/np.pi < 180:
            lab.set_rotation(angle*180/np.pi - 90)
        else:
            lab.set_rotation(angle*180/np.pi- 180 - 90)
        labels.append(lab)
    ax.set_xticklabels([])
    
    
    
    '''
    add tick labels to each radial axis
    '''
    
    #run through each angular line
    for i in range(len(Attributes)):
        
        labels = np.array(yticks).astype(float)*(data[Attributes[i]].max()-data[Attributes[i]].min()) + data[Attributes[i]].min()
    
    
        #run through each radial gridline
        for j in range(len(labels) - 1):
            
            
            #rotate the radial tick if needed
            if 180*angles[i]/np.pi < 180:
                
                a = 180*angles[i]/np.pi - 90
                
                ax.text(angles[i],np.array(yticks)[j + 1],'{}'.format(round(labels[j + 1],2)),
                        rotation = a,
                        fontsize = 10,
                        ha = 'center',
                        va = 'top')
                
            else:
        
                a = 180*angles[i]/np.pi - 90 - 180
                
                ax.text(angles[i],np.array(yticks)[j + 1],'{}'.format(round(labels[j + 1],2)),
                        rotation = a,
                        fontsize = 10,
                        ha = 'left',
                        va = 'center')
    
    '''
    plot the player spider plot onto radial graph
    '''
    
    k = 1;#initialise label count
    #run through each player
    for player in players:
        
        
        values = data_norm.loc[player].to_numpy()
        if values.shape[0] == AttNo:
            values = values.tolist();
            
        else:
            values = values[1].tolist()
        values += values[:1]
        
        #plot the line
        ax.plot(angles,values,
                color = colors['lineColor%d_alt'%k],
                alpha = 1)
        
        #fill for label
        ax.fill(angles, values,
                color = colors['lineColor%d'%k],
                edgecolor = colors['lineColor%d_alt'%k],
                alpha=0.3,
                label = player)
        
        #fill for outline, different alpha
        ax.fill(angles, values,
                alpha=1,
                facecolor = 'None',
                Hatch = '/',
                edgecolor = colors['lineColor%d_alt'%k],
                linewidth = 2)
        
        k +=1
        
        
    
    '''
    plot average
    '''
    
    values = data_norm.mean().tolist()
    values += values[:1]
    ax.plot(angles,values,
            ls = '--',
            color = 'gray',
            label = 'Average')
    
    ax.fill(angles, values,
            color = 'gray',
            alpha=0.1)
    
    ax.legend(bbox_to_anchor = (1.1,1.1),
              fontsize = 12,
              frameon = False)
    
    
    '''
    save figure
    '''
    
    if save == True:
        plt.savefig(Dir + '{}_vs_{}.png'.format(players[1],players[0]),bbox_inches='tight')
        
    return fig, ax


def pizza(data,Attributes,player,colors_ticks = None,params = params(),save = False, Dir = ''):
    """
    
    A program designed to plot the radar of up to two players against the average.
    
    Parameters
    -----------
                data: dataframe of the players data. Must have columns that 
                        are present in Attributes list
                Attributes: list of attributes or stats for slice axis plot
                player: string of player name that are within the 
                        data dataframe variable.
                colors_ticks: color scheme of each individual attribute label 
                            on plot. Default = None which leads to text color
                            ticks.
                params: dict of parameters used in the plot process
                save: bool for whether to save
                Dir: directory in which fig is save
    
    Returns
    -----------
                fig: matplotlib figure object of radar
                ax: matplotlib ax object of figure
    
    
    """
        
    #get the amount of slices of pizza
    N = data.shape[0]

    #construct the segements of the pizza using about of slices
    theta, width = np.linspace(0.0, 2 * np.pi, N, endpoint=False, retstep=True)
    
    #midpoints of slices
    angles = np.linspace(0.0, 2 * np.pi, N + 1 )
    
    
    """
    construct figure
    """
    
    fig = plt.figure(figsize = [10,10],dpi = 100)
    ax = fig.add_subplot(111, polar=True)
    
    
    """
    construct the title
    """
    fig.text(0.05,0.95,'Defensive, ',
              color = 'darkred',
              fontsize = 18,
              ha = 'left')
    fig.text(0.18, 0.95, 'Possession ',
              color = 'darkorange',
              fontsize = 18,
              ha = 'left')
    fig.text(0.32,0.95, 'and',
              color = 'black',
              fontsize = 18,
              ha = 'left')
    fig.text(0.37,0.95,'Final Product',
              color = 'darkblue',
              fontsize = 18,
              ha = 'left')
    fig.text(0.53,0.95,'statistics for {}'.format(player),
              color = 'black',
              fontsize = 18,
              ha = 'left')
    
    fig.text(0.05,0.1,'*% is accuracy of pass.',
              color = 'gray',
              fontsize = 12,
              ha = 'left')
    fig.text(0.05,0.075,'*All other stats are p90.',
              color = 'gray',
              fontsize = 12,
              ha = 'left')
    
    
    """
    add slices to the radial plot
    """
    bars = ax.bar(
        theta, data,
        width=width-0.03,
        color=colors_ticks, edgecolor="black",
        alpha = 0.7,
        zorder = 2
    )
    bars = ax.bar(
        theta, 100,
        width=width-0.03,
        color=colors_ticks, alpha=0.2,
        zorder = 0
    )
    
    
    
    """
    construct grid
    """
    ax.grid(ls = '--',zorder = 1)
    
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(1)
    
    ax.spines['polar'].set_visible(False)
    #ax.set_rticks([0,20,40,60,80,100])
    ax.set_rticks([0,20,40,60,80,100])
    ax.set_yticklabels([])
    
    
    #add the value labels to each slice
    for i in range(len(angles[:-1])):
        
        if data[i] > 0:
    
           ax.text(angles[i],data[i] - 1,'%d'%(data[i]),
                           fontsize = 14,
                           weight = 'bold',
                           ha = 'center',
                           va = 'center',
                           bbox = dict(facecolor='white', edgecolor='k',alpha = 0.9, boxstyle='round,pad=0.1'),
                           zorder = 5)
    
    plt.xticks(angles[:-1],Attributes, fontsize = 12)
    
    
    #add the labels to each slice
    labels = []
    for label, angle, color_tick in zip(ax.get_xticklabels(), angles,colors_ticks):
        x,y = label.get_position()
        lab = ax.text(x,y, label.get_text(), transform=label.get_transform(),
                      ha=label.get_ha(), va=label.get_va(),
                      color = color_tick,
                      fontsize = 10)
        
        if np.mod(angle*180/np.pi + 90,360) < 180:
            lab.set_rotation(angle*180/np.pi)
        else:
            lab.set_rotation(angle*180/np.pi- 180)
        labels.append(lab)
    ax.set_xticklabels([])
    
    
    if save == True:
        plt.savefig(Dir + '{}.png'.format(player),bbox_inches='tight')
    
    return fig,ax
