from QTA.Signals.ClassifyBar import ClassifyBar
from QTA.Signals.FindGap import FindGap
import QTA.DataConfiguration.RetrieveData as RD
import datetime as dt
import math as m

################################
# Unit Tests (FindGap)
################################

def test_calculate_gap_value():
    start = dt.datetime(2018, 1, 1)
    end = dt.datetime(2018, 1, 11)
    testData = RD.get_data('AAPL', start, end)
    
    gap = FindGap(testData.Open, testData.Close)
    result = gap.gap_Value()

    assert result[1] == 0.06750106811523438

def test_calculate_gap_percentage():
    start = dt.datetime(2018, 1, 1)
    end = dt.datetime(2018, 1, 11)
    testData = RD.get_data('AAPL', start, end)
    
    gap = FindGap(testData.Open, testData.Close)
    result = gap.gap_Percentage()

    assert result[1] == 0.15674229715026647

def test_check_gap_polarity():
    start = dt.datetime(2018, 1, 1)
    end = dt.datetime(2018, 1, 11)
    testData = RD.get_data('AAPL', start, end)
    
    gap = FindGap(testData.Open, testData.Close)
    result = gap.gap_Polarity()

    assert result[1] == True
