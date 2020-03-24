import quandl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
quandl.ApiConfig.api_key = 'taken out for security'
#Choose date range.
start = pd.to_datetime('2012-01-01')
end = pd.to_datetime('2018-03-27')
#Choose stocks.
aapl = quandl.get('WIKI/AAPL.11',start_date=start, end_date=end)
amzn = quandl.get('WIKI/AMZN.11',start_date=start, end_date=end)
fb = quandl.get('WIKI/FB.11',start_date=start, end_date=end)
googl = quandl.get('WIKI/GOOGL.11',start_date=start, end_date=end)
mfst = quandl.get('WIKI/MSFT.11',start_date=start, end_date=end)
#Concatenate stock adjusted close.
stocks = pd.concat([aapl,amzn,fb,googl,mfst], axis=1)
#Create log return and delete first row of null values.
log_ret = np.log(stocks/stocks.shift(1))
#Choose number of tries.
num_ports = 100000
#Initialize all possible values of weights for portfolio allocation.
all_weights = np.zeros((num_ports, len(stocks.columns)))
#Initialize return, volatility and Sharpe ratio arrays.
ret_arr = np.zeros(num_ports)
vol_arr = np.zeros(num_ports)
sharpe_arr = np.zeros(num_ports)
#Create simulation testing all random weights.
for ind in range(num_ports):
    weights = np.array(np.random.random(5))
    weights = weights/np.sum(weights)
    #Save weights
    all_weights[ind,:] = weights
    #Calculate expected return, volatility and Sharpe ratio.
    ret_arr[ind] = np.sum((log_ret.mean()*weights)*252)
    vol_arr[ind] = np.sqrt(np.dot(weights.T,np.dot(log_ret.cov()*252,weights)))
    sharpe_arr[ind] = ret_arr[ind]/vol_arr[ind]
#Print location of highest Sharpe ratio.
print(sharpe_arr.argmax())
#Use that location to find highest return and lowest volatility.
max_sr_ret = ret_arr[sharpe_arr.argmax()]
max_sr_vol = vol_arr[sharpe_arr.argmax()]
#Print best weights for portfolio allocation.
print("Best weights:")
print("AAPl, AMZN, FB, GOOGL, MSFT")
print(all_weights[sharpe_arr.argmax(),:])
#Create a scatterplot to find the highest return for the lowest volatility.
plt.figure(figsize=(12,8))
plt.scatter(vol_arr,ret_arr,c=sharpe_arr,cmap='plasma')
plt.colorbar(label='sharpe ratio')
plt.xlabel('volatility')
plt.ylabel('return')
plt.scatter(max_sr_vol,max_sr_ret,c='red')
plt.show()
