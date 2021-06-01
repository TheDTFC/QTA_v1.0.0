from QTA.Signals.ClassifyBar import ClassifyBar
from QTA.Execution.SetEntryExits import SetEntryExits
import QTA.DataConfiguration.RetrieveData as RD
import datetime as dt
import math as m

################################
# Unit Tests (SetEntryExits)
################################

def test_set_entry_price_from_buy_signal():
    start = dt.datetime(2018, 1, 1)
    end = dt.datetime(2018, 1, 11)
    testData = RD.get_data('AAPL', start, end)
    testData["Buy"] = testData["Open"] >= testData["Close"]
    
    buy = SetEntryExits(testData)
    result = buy.setPriceEntry()

    assert result[1] == 43.064998626708984

def test_set_target_price_from_entry_price():
    start = dt.datetime(2018, 1, 1)
    end = dt.datetime(2018, 1, 11)
    testData = RD.get_data('AAPL', start, end)
    testData["Buy"] = testData["Open"] >= testData["Close"]
    
    buy = SetEntryExits(testData)
    testData["PriceEntry"] = buy.setPriceEntry()
    target = buy.setPriceLimitTarget(0.02)

    assert target[1] == 43.92629859924317

def test_set_loss_price_from_entry_price():
    start = dt.datetime(2018, 1, 1)
    end = dt.datetime(2018, 1, 11)
    testData = RD.get_data('AAPL', start, end)
    testData["Buy"] = testData["Open"] >= testData["Close"]
    
    buy = SetEntryExits(testData)
    testData["PriceEntry"] = buy.setPriceEntry()
    target = buy.setPriceStopLoss(0.01)

    assert target[1] == 42.63434864044189

def test_trade_was_entered():
    return 
    
    pass

