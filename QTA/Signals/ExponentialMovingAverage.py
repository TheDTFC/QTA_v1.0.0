# -*- coding: utf-8 -*-
from pandas_datareader import data
import numpy as np
import pandas as pd
import datetime as dt
import QTA.DataConfiguration.RetrieveData as RD

class ExponentialMovingAverage:
    def __init__(self, alpha, stock_symbol, start_date, end_date):
        #the variable point_m is the interval the moving average is set
        self.alpha = alpha
        self.stock_symbol = stock_symbol
        self.start_date = start_date
        self.end_date = end_date

    def calculate_EMA_data(self):
        testData = RD.get_data(self.stock_symbol, self.start_date, self.end_date)
        dataClose = testData['Close']
        #print(type(dataClose))
        return dataClose

    def EMA_data(self):
        data1 = self.calculate_EMA_data().to_frame()
        data1['EMA_PointM'] = data1.ewm(alpha=self.alpha, adjust=False).mean()
        return data1