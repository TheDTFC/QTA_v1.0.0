
import filecmp
import os
import datetime as dt
import QTA.DataConfiguration.FormatData as FD
import QTA.DataConfiguration.RetrieveData as RD


def test_df_to_bar_list():

    start = dt.datetime(2019, 1, 2)
    end = dt.datetime(2020, 6, 2)
    result = RD.get_data('AAPL', start, end)

    bars = FD.create_bar_list(result)
    #i = 0
    #for i in range(len(bars)):
    #    print('date: ' + str(bars[i].date) + ' open: ' 
    #    + str(bars[i].open) + '  close: ' 
    #    + str(bars[i].close) )

    assert not (bars == None)

def test_output_to_csv():
    #Makes a data_frame from tsla, prints it to a csv and compares 
    #to existing one
    start = dt.datetime(2018, 1, 1)
    end = dt.datetime(2020, 6, 2)
    F1 = "tests/AAPL_correct.csv"

    result = RD.get_data('AAPL', start, end)
    FD.make_csv(result, 'AAPL')
    F2 = "AAPL.csv"

    assert filecmp.cmp(F1, F2)
    os.remove("AAPL.csv")

def test_ohlc():
    start = dt.datetime(2019, 1, 2)
    end = dt.datetime(2020, 6, 2)
    result = RD.get_data('AAPL', start, end)

    ohlc_df = FD.format_df(result)
    #print(ohlc_df.head)
    pass

def test_consolidate_bars():
    start = dt.datetime(2019, 1, 2)
    end = dt.datetime(2020, 6, 2)
    result = RD.get_data('AAPL', start, end)

    df_monthly = FD.consolidate_bars(result, '1M')
    #print(df_monthly.head)
    pass