import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

idea_df = pd.read_csv('IDEA.csv')

idea_df= idea_df[['date', 'close']]             #taking only the required coloumns to calcculate the gain/return

idea_df = idea_df.set_index(pd.DatetimeIndex(idea_df['date'], dayfirst=True))    #dayfirst=true gets the date into the indian style which is ddmmyyyy


plt.figure(figsize=(12,5))                                    # the default figsize provided by the matplot is smaller
plt.plot(idea_df.index, idea_df.close)                  # as the date is set as an index so took it
plt.xlabel('Date')
plt.ylabel('Close')
plt.show()

#for calculating  the daily returns we will calculate the percentage change of the close price of the stock on that particular day vs yesterday

#use the pct_change() method of pandas
gain = idea_df['close'].pct_change(periods=1)     # periods=1 tells that you have to take the previous value

plt.figure(figsize=(12,5))
plt.plot(idea_df.index, gain)
plt.xlabel('Date')
plt.ylabel('Gain')
plt.show()


#we will get the gain in the range of -1 to +1


#For range of gain at a specific confidence interval :
from scipy import stats

#take the confidence interval from the user and calculate the range of gain
#for normal distribution the location parameter is the mean
#for normal distribution the scale parameter is the standard deviation

conf= float(input("Enter the Confidence percent(in decimal):"))

idea_df_ci = stats.norm.interval(conf, loc=idea_df.gain.mean(), scale=idea_df.gain.std())

print("The range of  gain in the confidence interval is: ",np.round(idea_df_ci,4))



