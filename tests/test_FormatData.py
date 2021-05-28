import datetime as dt
import QTA.DataConfiguration.FormatData as FD

def test_df_to_bar_list():

    start = dt.datetime(2019, 1, 2)
    end = dt.datetime(2020, 6, 2)
    result = FD.get_data('AAPL', start, end)

    bars = FD.create_bar_list(result)
    #i = 0
    #for i in range(len(bars)):
    #    print('date: ' + str(bars[i].date) + ' open: ' 
    #    + str(bars[i].open) + '  close: ' 
    #    + str(bars[i].close) )

    assert not (bars == None)