import datetime as dt
import pandas as pd
from numpy import NaN

import QTA.DataConfiguration.RetrieveData as RD
import QTA.Signals.FindGap
import QTA.Signals.ClassifyBar
import QTA.Execution.SetEntryExits



################ MODIFY SECTION BELOW TO TEST DIFFERENT DATES/EQUITIES ####################

start = dt.datetime(2019, 1, 1)
end = dt.datetime(2020, 1, 1)
ticker_symbol = 'AAPL'

################ END OF MODIFICATION SECTION ####################



# Get Data and Reset date index
ohlc = RD.get_data(ticker_symbol, start, end)
ohlc.reset_index(inplace=True)
ohlc = ohlc.reset_index(drop=True)

print(ohlc.head())



################ MODIFY SECTION BELOW TO TEST DIFFERENT TEST STRATEGIES ####################
            ### ONLY SET 1 ohlc['Buy'] TO RUN TEST, COMMENT OTHERS ###

# Define Strategy Test 1 - Using a positive GAP polarity to set the Buy Trigger
FG = QTA.Signals.FindGap.FindGap(ohlc.Open,ohlc.Close)
#ohlc['Buy'] = FG.gap_Polarity()

# Define Strategy Test 2 - Using a positive BAR polarity to set the Buy Trigger
CB = QTA.Signals.ClassifyBar.ClassifyBar(ohlc.Open,ohlc.Close,ohlc.High,ohlc.Low,ohlc.Volume)
#ohlc['Buy'] = CB.polarity()

# Define Strategy Test 3 - Using a bullish engulfing pattern to set the Buy Trigger
ohlc['Buy'] = CB.bullish_engulfing_pattern()
print(ohlc.head(50))

################ END OF MODIFICATION SECTION ####################



# Functions to set/update the Price Entry, Trade Status, Targets/Stops
SEE = QTA.Execution.SetEntryExits.SetEntryExits(ohlc)
ohlc['numTradesEntered'] = 0



################ MODIFY SECTION BELOW TO TEST DIFFERENT R:R PARAMETERS ####################

# Set Test Input Parameters
maxReward = 5 # in percent
minReward = 1 # in percent
rewardIncrement = 1
maxRisk = (2)*2 # in percent (multiplied by 2 since its divided by 2 in the For Loop)
minRisk = (1)*2 # in percent (multiplied by 2 since its divided by 2 in the For Loop)
riskIncrement = 1

################ END OF MODIFICATION SECTION ####################


summary = []

# Iterate through various Reward/Risk Scenarios
for x in range(minRisk,maxRisk+1,riskIncrement):
    for y in range(minReward,maxReward+1,rewardIncrement):
        print('> Ticker: ' + ticker_symbol)
        
        outputList = SEE.findExitWinsLosses(y/100, x/200)
        lst = [ticker_symbol,outputList[0],outputList[5],outputList[6],outputList[7],round(y/1.0,1),round(x/2,1),outputList[4],outputList[1],outputList[2],outputList[3]]
        summary.append(lst)

summaryOutput = pd.DataFrame(summary, columns=['Ticker','NumTrds','AvgWPer','AvgLPer','%NumPer','Reward%','Risk%','R:R','Winrate%','Ret/Trd%', 'Ret%'])

csv = summaryOutput.sort_values(['Ret/Trd%','Winrate%'],ascending=[False,False])
csv.to_csv(ticker_symbol + '_Summary.csv')

print(summaryOutput.sort_values(['Ret/Trd%','Winrate%'],ascending=[False,False]).head(10))
print(summaryOutput.sort_values(['Winrate%','Ret/Trd%'],ascending=[False,False]).head(10))
