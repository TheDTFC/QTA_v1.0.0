import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance.original_flavor
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
import numpy as np
from findiff import FinDiff
import QTA.DataConfiguration.RetrieveData as RD

def plot(symbol, start, end):

    df = RD.get_data(symbol, start, end)

    df_ohlc = df['Adj Close'].resample('7D').ohlc()
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
    ax1.xaxis_date()

    candlestick_ohlc(ax1, df_ohlc.values, width=4, colorup='g')
    ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0) 
    ax1.plot(df_200ma.index.map(mdates.date2num), df_200ma.values)
    ax1.plot(df_21ma.index.map(mdates.date2num), df_21ma.values)

    df.plot()
    plt.show()
