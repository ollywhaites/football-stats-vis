# Football Statistics Visualisation

This file contains three slightly different methods of visualising players stats over a season. These can be utilised to staitsically flag players for scouting by comparing players in similar leagues. Additionally, it can be used to compare player's statistics between different seasons in order to highlight how a player has developed over time and help aid their development.

*All methods in this document are not assumed to be unique, but instead review how they may be constructed and used to evaluate players. Specific details of code and presentation have been created by Oliver Whaites.*

*Data used in this documents belongs to Wyscout.*

## Data used

This file uses statistics of players from Wyscout, specifically for Declan Rice in the 2021-22 and 2020-21 Premier League seasons. The data is filtered into players who have played as a central midfielder (keyed as CM in Wyscout) in these season. Any player that has played less that 1000 mins is truncated as they can have inflated statistics when normalising to per 90.

Unless stated otherwise, the statistics used are normalised to per 90 or percentage accuracy/success (denoted by ,%). Normalisation to per 90 helps judge players fairly, as someone who has played 4000 mins has had more opportunity to score than someone who has played 3000 mins. Success percentages give a good indication of how 'good' a player is at that particular stat. For example, a player may make a lot of long passes, but the true measure is how accurate those long passes are. However, this type of statistic must be used carefully as players who have attempted few of a particular statistic (e.g few long passes) may have a skewed success percentage value.

## Player Radars

Player radars are a commonly used method to evaluate the playstyle and quality of a player. Player statistics are displayed on a radial plot, where the further the line is away from the centre larger the numerical value of the statistic is. All players in the dataset are normalised in each statitsic, such that the outer values in the radar are the maximum in the dataset and the inner values are the minimum. For the majority of statistics larger numeric values signify that how good a player is at that statistic, howeve in general this is not always the case (e.g Yellow Cards, Fouls, ...). In order to evaluate the quality of a player in each statistic, the base level of players in the league in that season are plotted as the mean values, denoted as a dahsed grey line. Bellow is an example of a player radar.


![D  Rice_vs_W  Ndidi](https://user-images.githubusercontent.com/110287328/182711667-510248d9-f206-425d-b792-b7aeeb98d253.png)


This radar compares the quality and playstyle of Declan Rice of West Ham United and Wilfred Ndidi of Leicester City for the 2021-2022 Premier League season. Differences in their stats gives us insight into who may be better at certain parts of the game or difference in playstyle. In the above radar, Declan Rice's passing statsistics are shown to better that of Ndidi's. Rice is shown to be one of the top players for passing accuracy stats in the 2021-2022 season, where he is the best for Forward pass accuracy and very highly rated for the majority of other passing accuracies. Whereas Ndidi has sub-average passing stats in all catagories except for lateral passes. From this we can gather that Ndidi may not get involved in Leicesters build up play and may only shunt the ball to nearby midfielders. Rice may be seen to get on the ball more and inspire some of West Ham United's build up play, echoed in his above average assisting statistics. 

Moreover, Ndidi has exceptional definding statistics making nearly 8 Possession adjusted interceptions per 90 mins, one of the best in the league. Although Rice's defensive stats are good, and above average, they do not match that of Ndidi's. This may come down to their playstyle. We can gather that Ndidi is excellent at winning possesion back for Leicester, but does not aim to spur on the offensive. He seems more likely to shunt the ball to his midfield partner and allow them to be creative. On the other hand, Declan Rice is effective at winning possession back, but is more likely to either look for the pass or drive the ball up the pitch towards the oppositions box; something that is evident in his progressive runs and offensive duels per 90 mins.

*It is worth noting that the area of the radar does not fully represent how good a player is. This is because it is dependent on the ordering of the angular axis. If all the players favoured stats are grouped together, then the area at one side of the radar will be large and 'look more appealling'. On the other hand, alternating players dominant stats will give the appearance of a spikey radar, thus 'looking worse'. The user must be careful and only consider how the player ranks in each statistic separately.*

## Pizza Plot

One limitation of the radar plot is the influence of any extreme outliers. For example, there may be one player in the league who is far superior in assists than anyone else in the league. In a player radar, this may make other players look worse than they actually are. Mainly because the radar has no information about how the statistics for the players are distributed. 

The pizza plot aims to address this limitation. Rather than showng the raw value of a particular statistic, the pizza plot displays the player percentile in a statistic. This means that the best player in that statitsic will score 100 and the worst will score 0. Consequently average players should fall around the 50 mark. With this change, a dominant player in that statitsic will score 100, whereas the next player will score 99 even if they are far less superior. An example of two Pizza plots for Declan Rice and Wilfred Ndidi are shown bellow. They are separate so not to make each plot too 'busy'.


Declan Rice             |  Wilfred Ndidi
:-------------------------:|:-------------------------:
![D  Rice](https://user-images.githubusercontent.com/110287328/182711303-4744f0d5-3e6b-473d-a42d-35bbf3d54480.png) |   ![W  Ndidi](https://user-images.githubusercontent.com/110287328/182711349-77be4295-be2d-481d-8f65-0703469b9d6f.png)


This plot has given us more information about the two players. In the radar plot, the final product (blue) statistics look low for both players and even the average. Most likely, this is due to a few outlying performers who have drastically higher statitsics. Looking at the pizza plot shows that in fact Rice performs well in these areas, achieving the 87th percentile for expected assist (xA) per key pass and the 84th percentile for Second/Third Assists. Further issues may arise when looking at the passing, which for Ndidi is further away from the centre of the radar (creating a larger area) than some of his creative stats, whereas the pizza plot highlights that he is in roughly the same percentile for both. It is worth noting that this is visible in the radar plot (see that Rice's stats fall above average), yet the pizza plot displays this fact clearer. 

There are pros and cons to both of these plots. Altough clearer, the pizza plot does not exhibit any raw statistcial value, hence not informing the user how the player truely plays. Moreover, it could be argued that outlying players deserve to be represented fairly, as it is evidence for how much better they are. In practice, both of these visualisations have their place and should be used in tamden to gain full information of a players ability and playstyle. Bellow is a breif summary of the pros and cons of the previous two methods.

Radar Plots       |Pizza Plots         
|-----------------|-------------------|
|- Displays raw information |- Can remove outlying performers|
|- Can compare two players in one figure|- Clearly displays players strengths|
|- Can infer playstyle | - Can infer playstyle|


## Distribution Plot

![D  Rice_vs_W  Ndidi_dist_plot](https://user-images.githubusercontent.com/110287328/182716133-7d99f497-8954-4e5b-82d9-b674480d93d2.png)



