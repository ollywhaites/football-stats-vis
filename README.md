# Football Statistics Visualisation

This file contains three slightly different methods of visualising players stats over a season. These can be utilised to staitsically flag players for scouting by comparing players in similar leagues. Additionally, it can be used to compare player's statistics between different seasons in order to highlight how a player has developed over time and help aid their development.

*All methods in this document are not assumed to be unique, but instead review how they may be constructed and used to evaluate players. Specific details of code and presentation have been created by Oliver Whaites.*

*Data used in this documents belongs to Wyscout.*

## Data used

This file uses statistics of players from Wyscout, specifically for Declan Rice in the 2021-22 and 2020-21 Premier League seasons. The data is filtered into players who have played as a central midfielder (keyed as CM in Wyscout) in these season. Any player that has played less that 1000 mins is truncated as they can have inflated statistics when normalising to per 90.

Unless stated otherwise, the statistics used are normalised to per 90 or percentage accuracy/success (denoted by ,%). Normalisation to per 90 helps judge players fairly, as someone who has played 4000 mins has had more opportunity to score than someone who has played 3000 mins. Success percentages give a good indication of how 'good' a player is at that particular stat. For example, a player may make a lot of long passes, but the true measure is how accurate those long passes are. However, this type of statistic must be used carefully as players who have attempted few of a particular statistic (e.g few long passes) may have a skewed success percentage value.

## Player Radars

Player radars are a commonly used method to evaluate the playstyle and quality of a player. Player statistics are displayed on a radial plot, where the further the line is away from the centre larger the numerical value of the statistic is. All players in the dataset are normalised in each statitsic, such that the outer values in the radar are the maximum in the dataset and the inner values are the minimum. For the majority of statistics larger numeric values signify that how good a player is at that statistic, howeve in general this is not always the case (e.g Yellow Cards, Fouls, ...). In order to evaluate the quality of a player in each statistic, the base level of players in the league in that season are plotted as the mean values, denoted as a dahsed grey line. Bellow is an example of a player radar.


![Wilfrid Ndidi vs Declan Rice](https://user-images.githubusercontent.com/110287328/182382250-a2a519de-4fe7-489a-ad77-540305e2162d.png)

This radar compares the quality and playstyle of Declan Rice of West Ham United and Wilfred Ndidi of Leicester City for the 2021-2022 Premier League season. Differences in their stats gives us insight into who may be better at certain parts of the game or difference in playstyle. In the above radar, Declan Rice's passing statsistics are shown to better that of Ndidi's. Rice is shown to be one of the top players for passing accuracy stats in the 2021-2022 season, where he is the best for Forward pass accuracy and very highly rated for the majority of other passing accuracies. Whereas Ndidi has sub-average passing stats in all catagories except for lateral passes. From this we can gather that Ndidi may not get involved in Leicesters build up play and may only shunt the ball to nearby midfielders. Rice may be seen to get on the ball more and inspire some of West Ham United's build up play, echoed in his above average assisting statistics. 

Moreover, Ndidi has exceptional definding statistics making nearly 8 Possession adjusted interceptions per 90 mins, one of the best in the league. Although Rice's defensive stats are good, and above average, they do not match that of Ndidi's. This may come down to their playstyle. We can gather that Ndidi is excellent at winning possesion back for Leicester, but does not aim to spur on the offensive. He seems more likely to shunt the ball to his midfield partner and allow them to be creative. On the other hand, Declan Rice is effective at winning possession back, but is more likely to either look for the pass or drive the ball up the pitch towards the oppositions box; something that is evident in his progressive runs and offensive duels per 90 mins.



## Pizza Plot

![S  Deadfield](https://user-images.githubusercontent.com/110287328/182389989-1e46f29b-63a0-4053-9573-d26b55bc2c06.png)


## Distribution Plot

![sam_deadfield](https://user-images.githubusercontent.com/110287328/182390108-c6ff9c86-0372-4c04-b3cd-5cff8210921a.png)

