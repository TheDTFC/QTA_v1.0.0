import datetime as dt
import QTA.DataConfiguration.RetrieveData as RD
from QTA.Signals.ExponentialMovingAverage import ExponentialMovingAverage

def test_display_data():
    EMA = ExponentialMovingAverage(0,'AAPL', dt.datetime(2018, 1, 1), dt.datetime(2018, 5, 3))
    EMA.calculate_EMA_data()

def test_EMA_data():
    EMA = ExponentialMovingAverage(.5,'AAPL', dt.datetime(2018, 1, 1), dt.datetime(2018, 1, 20))
    EMA.EMA_data()

def test_no_variation():
     EMA = ExponentialMovingAverage(1,'AAPL', dt.datetime(2018, 1, 1), dt.datetime(2018, 12,31))
     EMA_1 = EMA.EMA_data() 
     assert(EMA_1['Close'].equals(EMA_1['EMA_PointM']))

def test_variation_of_2():
     EMA = ExponentialMovingAverage(.2,'AAPL', dt.datetime(2018, 1, 1), dt.datetime(2018, 1, 5))
     EMA_1 = EMA.EMA_data()
     assert(EMA_1['EMA_PointM'].to_list() == [43.064998626708984, 43.06349868774414, 43.10229888916016, 43.23183911132813])

def test_variation_greater_than_2():
     SMA = ExponentialMovingAverage(.5,'AAPL', dt.datetime(2018, 1, 1), dt.datetime(2018, 1, 5))
     EMA_1 = SMA.EMA_data()
     assert(EMA_1['EMA_PointM'].to_list() == [43.064998626708984, 43.061248779296875, 43.15937423706055, 43.45468711853027])