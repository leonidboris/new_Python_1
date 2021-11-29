

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#from google.colab import files
#uploaded = files.upload()

df = pd.read_csv('M:\AUDUSD1440.csv')




# print(df)

plt.figure(figsize=(13,5))
plt.plot(df['close'], label = 'close')
plt.xlabel('17.12.2017-23.11.2021')
plt.ylabel('close usd ($)')
plt.legend(loc='upper left')
#plt.show()



sma1 = pd.DataFrame()
sma1['sma1'] = df['close'].rolling(window=1).mean()
sma50 = pd.DataFrame()
sma50['sma50'] = df['close'].rolling(window=50).mean()
sma100 = pd.DataFrame()
sma100['sma100'] = df['close'].rolling(window=100).mean()
sma200 = pd.DataFrame()
sma200['sma200'] = df['close'].rolling(window=200).mean()




plt.figure(figsize=(13,5))
plt.plot(df['close'], label = 'close')
plt.plot(sma1['sma1'], label = 'sma1')
plt.plot(sma50['sma50'], label = 'sma50')
plt.plot(sma100['sma100'], label = 'sma100')
plt.plot(sma200['sma200'], label = 'sma200')
plt.title('all close price')
plt.xlabel('17.12.2017-23.11.2021')
plt.ylabel('close usd ($)')
plt.legend(loc='upper left')
plt.show()


df1 = pd.DataFrame()
df1['date'] = df['date']
df1['close'] = df['close']
df1['sma1'] = sma1['sma1']
df1['sma50'] = sma50['sma50']
df1['sma100'] = sma100['sma100']
df1['sma200'] = sma200['sma200']


def dual_sma(df1):
    buy_signal_price = []
    sell_signal_proce = []
    flag = 0

    for i in range(len(df)):
        if (
           (df1['close'][i] > df1['sma50'][i])
            and
           (df1['sma50'][i] > df1['sma100'][i])
#            and
#           (df1['sma100'][i] > df1['sma200'][i])
           ):
            if flag != 1:
                buy_signal_price.append(df1['close'][i])
                sell_signal_proce.append(np.nan)
                flag = 1
            else:
                buy_signal_price.append(np.nan)
                sell_signal_proce.append(np.nan)
        elif (
           (df1['close'][i] < df1['sma50'][i])
            and
           (df1['sma50'][i] < df1['sma100'][i])
#            and
#           (df1['sma100'][i] < df1['sma200'][i])
            ):
            if flag !=  -1:
                buy_signal_price.append(np.nan)
                sell_signal_proce.append(df1['close'][i])
                flag = -1
            else:
                buy_signal_price.append(np.nan)
                sell_signal_proce.append(np.nan)
        else:
            buy_signal_price.append(np.nan)
            sell_signal_proce.append(np.nan)
        return(buy_signal_price,sell_signal_proce)



dual_sma = dual_sma(df1)
df1['buy signal prices'] = dual_sma[0]
df1['sell signal prices'] = dual_sma[1]

plt.figure(figsize=(13,5))
plt.plot(df['close'], label = 'close', alpha = 0.6)
plt.plot(sma50['sma50'], label = 'sma50', linewidths=3)
plt.plot(sma100['sma100'], label = 'sma100', linewidths=3)
plt.plot(sma200['sma200'], label = 'sma200', linewidths=3)
plt.scatter(df1.index,df1['buy signal price'], label = 'buy', color = 'blue', marker = '^', linewidths=5 )
plt.scatter(df1.index,df1['sell signal price'], label = 'sell', color = 'red', marker = 'V', linewidths=5 )
plt.title('all close price')
plt.xlabel('17.12.2017-23.11.2021')
plt.ylabel('close usd ($)')
plt.legend(loc='upper left')
plt.show()
