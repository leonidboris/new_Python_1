

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
plt.show()



sma1 = pd.DataFrame()
sma1['close'] = df['close'].rolling(window=1).mean()
sma50 = pd.DataFrame()
sma50['close'] = df['close'].rolling(window=50).mean()
sma100 = pd.DataFrame()
sma100['close'] = df['close'].rolling(window=100).mean()
sma200 = pd.DataFrame()
sma200['close'] = df['close'].rolling(window=200).mean()


plt.figure(figsize=(13,5))
plt.plot(df['close'], label = 'close')
plt.plot(sma50['close'], label = 'close_sma50')
plt.plot(sma100['close'], label = 'close_sma100')
plt.plot(sma200['close'], label = 'close_sma200')
plt.xlabel('17.12.2017-23.11.2021')
plt.ylabel('close usd ($)')
plt.legend(loc='upper left')
plt.show()


df1 = pd.DataFrame()
df1['close'] = df['close']




def dual_sma(df):
    buy_signal_price = []
    sell_signal_proce = []
    flag = 0

    for i in range(len(df)):
        if df['sma1'][i] > df['sma50'][i]:
            if flag != 1:
                buy_signal_price.append(df['close'][i])
                sell_signal_proce.append(np.nan)
                flag = 1
            else:
                buy_signal_price.append(np.nan)
                sell_signal_proce.append(np.nan)
        elif df['sma1'][i] < df['sma50'][i]:
            if flag !=  -1:
                buy_signal_price.append(np.nan)
                sell_signal_proce.append(df['close'][i])
                flag = -1
            else:
                buy_signal_price.append(np.nan)
                sell_signal_proce.append(np.nan)
        else:
            buy_signal_price.append(np.nan)
            sell_signal_proce.append(np.nan)
        return(buy_signal_price,sell_signal_proce)

    dual_sma = dual_sma(df)