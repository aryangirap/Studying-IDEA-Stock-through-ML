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


#For calculating the risk We use the standard deviation higher the standard deviation higher is the risk

print("The standard deviation of the gain is : ", np.round(idea_df.gain.std(),6))

print("The Mean of the gain is : ", np.round(idea_df.gain.mean(),6))

# Now using the monte carlo simulation to simulate the close price of the IDEA stock of the next 5 years
log_ret = np.log(idea_df['close'] / idea_df['close'].shift(1)).dropna()
mu = log_ret.mean()
sigma = log_ret.std()

days = 252 * 5
n_sims = 1000
np.random.seed(42)

shocks = np.random.normal(mu, sigma, size=(days, n_sims))
paths = idea_df['close'].iloc[-1] * np.exp(np.cumsum(shocks, axis=0))

future_dates = pd.bdate_range(idea_df.index[-1] + pd.Timedelta(days=1), periods=days)
p5, p50, p95 = np.percentile(paths, [5, 50, 95], axis=1)

plt.figure(figsize=(12, 5))
plt.plot(idea_df.index, idea_df['close'], label='Historical Close')
plt.plot(future_dates, paths[:, :30], color='grey', alpha=0.15)
plt.plot(future_dates, p50, color='red', label='Median path')
plt.fill_between(future_dates, p5, p95, color='orange', alpha=0.3, label='5%-95% range')
plt.xlabel('Date')
plt.ylabel('Close')
plt.legend()
plt.show()



