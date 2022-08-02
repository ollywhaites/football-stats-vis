# Football Statistics Visualisation

This file contains three slightly different methods of visualising players stats over a season. These can be utilised to staitsically flag players for scouting by comparing players in similar leagues. Additionally, it can be used to compare player's statistics between different seasons in order to highlight how a player has developed over time and help aid their development.

*All methods in this document are not assumed to be unique, but instead review how they may be constructed and used to evaluate players. Specific details of code and presentation have been created by Oliver Whaites.*

*Data used in this documents belongs to Wyscout.*

## Data used

This file uses statistics of players from Wyscout, specifically for Declan Rice in the 2021-22 and 2020-21 Premier League seasons. The data is filtered into players who have played as a central midfielder (keyed as a CM in Wyscout) in these season. Any player that has played less that 1000 mins is truncated as they can have inflated statistics when normalising to per 90.

Unless stated otherwise, the statistics used are normalised to per 90 or percentage accuracy/success (denoted by ,%). Normalisation to per 90 helps judge players fairly, as someone who has played 4000 mins has had more opportunity to score than someone who has played 3000 mins. Success percentages give a good indication of how 'good' a player is at that particular stat. For example, a player may make a lot of long passes, but the true measure is how accurate those long passes are. However, this type of statistic must be used carefully as players who have attempted few of a particular statistic (e.g few long passes) may have a skewed success percentage value.

## Player Radars

Player radars are a commonly used method to evaluate the playstyle and quality of a player. Player statistics are displayed on a radial plot, where the further the line is away from the centre larger the numerical value of the statistic is. All players in the dataset are normalised in each statitsic, such that the outer values in the radar are the maximum in the dataset and the inner values are the minimum. For the majority of statistics larger numeric values signify that how good a player is at that statistic, howeve in general this is not always the case (e.g Yellow Cards, Fouls, ...). In order to evaluate the quality of a player in each statistic, the base level of players in the league in that season are plotted as the mean values, denoted as a dahsed grey line. 

![A test image](C. Paul_vs_D. Deadfield.png)
