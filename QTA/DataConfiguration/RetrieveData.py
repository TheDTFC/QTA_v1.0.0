from pandas_datareader import data
import pandas as pd
import datetime as dt


def get_data(symbol = 'AAPL', start = dt.datetime(2015, 1, 1), 
    end = dt.datetime(2018, 2, 8)):

    data_frame = data.DataReader(symbol, 'yahoo', start, end)

    return data_frame

def check_dates(start, end):
    if(start < end):
        return True
    return False
