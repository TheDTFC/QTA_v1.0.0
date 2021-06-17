import datetime as dt
import QTA.DataConfiguration.RetrieveData as RD
from QTA.Signals.SimpleMovingAverage import SimpleMovingAverage

def test_display_data():
    SMA = SimpleMovingAverage(0,'AAPL', dt.datetime(2018, 1, 1), dt.datetime(2018, 5, 3))
    SMA.calculate_SMA_data()

def test_SMA_data():
    SMA = SimpleMovingAverage(2,'AAPL', dt.datetime(2018, 1, 1), dt.datetime(2018, 1, 20))
    SMA.SMA_data()

def test_no_variation():
     SMA = SimpleMovingAverage(1,'AAPL', dt.datetime(2018, 1, 1), dt.datetime(2018, 12,31))
     SMA_1 = SMA.SMA_data() 
     assert(SMA_1['Close'].equals(SMA_1['SMA_PointM']))

def test_variation_of_2():
     SMA = SimpleMovingAverage(2,'AAPL', dt.datetime(2018, 1, 1), dt.datetime(2018, 1, 5))
     SMA_1 = SMA.SMA_data()
     assert(SMA_1['SMA_PointM'].to_list() == [43.064998626708984, 43.061248779296875, 43.15749931335449, 43.50374984741211])

def test_variation_greater_than_2():
     SMA = SimpleMovingAverage(5,'AAPL', dt.datetime(2018, 1, 1), dt.datetime(2018, 1, 10))
     SMA_1 = SMA.SMA_data()
     assert(SMA_1['SMA_PointM'].to_list() == [43.064998626708984, 43.061248779296875,43.12666575113932, 43.28249931335449,43.343499755859376,43.447000122070314,43.55])
