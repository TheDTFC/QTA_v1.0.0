# -*- coding: utf-8 -*-
from pandas_datareader import data
import numpy as np
import pandas as pd
import datetime as dt
import QTA.DataConfiguration.RetrieveData as RD


class SimpleMovingAverage:
    def __init__(self, point_m, stock_symbol, start_date, end_date):
        #the variable point_m is the interval the moving average is set
        self.point_m = point_m
        self.stock_symbol = stock_symbol
        self.start_date = start_date
        self.end_date = end_date

    def calculate_SMA_data(self):
        testData = RD.get_data(self.stock_symbol, self.start_date, self.end_date)
        dataClose = testData['Close']
        #print(type(dataClose))
        return dataClose

    def SMA_data(self):
        data1 = self.calculate_SMA_data().to_frame()
        data1['SMA_PointM'] = data1.rolling(self.point_m, min_periods=1).mean()
        return data1



