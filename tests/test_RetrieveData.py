import datetime as dt
import QTA.DataConfiguration.RetrieveData as RD



def test_read_data_from_yahoo():
    #checks to make sure the dataframe is returned
    start = dt.datetime(2018, 1, 1)
    end = dt.datetime(2020, 6, 2)

    result = RD.get_data('AAPL', start, end)

    assert (result.empty == False)

def test_input_start_date_is_before_end():
    start = dt.datetime(2018, 1, 5)
    end = dt.datetime(2020, 6, 2)
    result = RD.check_dates(start, end)

    assert result == True

def test_input_end_date_is_valid():
    start = dt.datetime(2018, 1, 1)
    end = dt.datetime(2020, 6, 2)
    result = RD.get_data('AAPL', start, end)

    assert (result.iloc[-1].name == dt.datetime(2020, 6, 2))

