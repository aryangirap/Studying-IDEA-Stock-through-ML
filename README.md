# Studying-IDEA-Stock-through-ML
understanding the ML Concept of "Gaussian"(Normal) distribution in which i am going to plot a graph on the basis of the close prices of the "IDEA" stock which i got from KAGGLE and understand its daily return, volitality and probability of making daily return of x percentage anf range of return at a certain confidence interval


For daily return(gain) i used the pct_change()  method of pandas to get the gain by calculating the percentage change of close price(today) and closeprice(yesterday)
The percentage change is from -1 to 1 

Confidence Interval: suppose the confidence interval is 90% so the remaining 10% is split into two (5% + 5%) first 5% is forthe extreme good values(extreme profit) and the second 5% is the extreme bad values(extreme loss) so this 10% are ignored and only the remaining 90%'s evaluated based on their gain

I used the scipy library and from that i used the stats module and as the graph is on normal distribution i accessed the stats.norm 
For the confidence interval i used the interval() method from the stats.norm 

interval()  has 3 parameters 
1. Alpha: We have to enter the confidence percent in decimal
2. Location : as there is a normal distribution the location parameter is the mean
3. Scale: as there is a normal distribution the Scale parameter is the standard deviation

For the idea stock i got :
Enter the Confidence percent(in decimal):0.95
The range of  gain in the confidence interval is:  [-0.0721  0.0728]
