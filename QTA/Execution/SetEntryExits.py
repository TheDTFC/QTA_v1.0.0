from numpy import NaN
import pandas_datareader

class SetEntryExits:
    def __init__(self, df_total):
        self.df = df_total
    
    def findExitWinsLosses(self,reward,risk):     

        # Create Price Entry and Exit arrays to store values
        SL = [] # Stop Loss
        LT = [] # Limit Target
        PEnter = [] # Price Entry
        PDateEntered = [] # Price Entry Date
        DateWin = []
        DateLoss = []
        tradeLengthCounter = []
        tradeWinLength = []
        tradeLossLength = []
        SPL = [] # Sell Price Losses
        SPW = [] # Sell Price Wins
        sellProfit = [] # Sell Profit (dollars)
        sellLoss = [] # Sell Loss (dollars)
        firstRow = 0
        

        # Loop through all rows to update Price Entries and Exits
        for index, row in self.df.iterrows():
            # To bypass indexing error on first row
            if firstRow != 0:
                # Adding a Price Entry/Target/Stop to each array
                if self.df.loc[index-1,'Buy'] == True:
                    # Incrementing numTradesEntered to use for future loop conditions 
                    self.df.loc[index,'numTradesEntered'] = self.df.loc[index-1,'numTradesEntered'] + 1
                    self.df.loc[index,'PriceEntered'] = self.df.loc[index-1,'Close']
                    
                    # Adding Prices to arrays
                    PEnter.append(round(self.df.loc[index,'PriceEntered'],4))
                    PDateEntered.append(self.df.loc[index,'Date'])
                    self.df.loc[index,'LimitTarget'] = round(self.df.loc[index,'PriceEntered'] * (1+reward),4)
                    LT.append(round(self.df.loc[index,'LimitTarget'],4))
                    self.df.loc[index,'StopLoss'] = round(self.df.loc[index,'PriceEntered'] * (1-risk),4)
                    SL.append(round(self.df.loc[index,'StopLoss'],4))
                    tradeLengthCounter.append(1)
                else:
                    # Update numTradesEntered
                    self.df.loc[index,'numTradesEntered'] = self.df.loc[index-1,'numTradesEntered']
            else:
                firstRow = 1

            # Initialize Sell flag
            sellFlag = 0

            # Loop through dataframe and Stop array to find when a bar has dipped below the Stop price
            for i in range(len(SL)):
                if (self.df.loc[index,'numTradesEntered'] > 0) & (self.df.loc[index,'Low'] < SL[i]) & (SL[i] != 0):
                    sellFlag = 1
                    SPL.append(SL[i])
                    sellLoss.append(round((-1)*SL[i]*risk/(1-risk),4))                    
                    SL[i] = 0
                    LT[i] = 0
                    tradeLossLength.append(tradeLengthCounter[i])
                    tradeLengthCounter[i] = NaN
                    DateLoss.append(PDateEntered[i])
                    self.df.loc[index,'numTradesEntered'] = self.df.loc[index,'numTradesEntered'] - 1
                elif (self.df.loc[index,'numTradesEntered'] > 0) & (self.df.loc[index,'High'] > LT[i]) & (LT[i] != 0):
                    sellFlag = 1
                    SPW.append(LT[i])
                    sellProfit.append(round(LT[i]*reward/(1+reward),4))  
                    SL[i] = 0
                    LT[i] = 0
                    tradeWinLength.append(tradeLengthCounter[i])
                    tradeLengthCounter[i] = NaN
                    DateWin.append(PDateEntered[i])
                    self.df.loc[index,'numTradesEntered'] = self.df.loc[index,'numTradesEntered'] - 1                
                else:    
                    if tradeLengthCounter[i] == NaN:
                        pass
                    else:
                        tradeLengthCounter[i] = tradeLengthCounter[i] + 1
            
            # Updating the Sell status in the main dataframe
            if sellFlag == 1:
                self.df.loc[index,'Sell'] = True
            else:
                self.df.loc[index,'Sell'] = False 


        """ """
        # FOR DEBUGGING
        print('\n>  SL:\n%s' % SL)
        print('\n>  LT:\n%s' %LT)
        print('\n>  PEnter: ' + str(len(PEnter)))
        print(PEnter)
        print('\n>  PDateEntered: ' + str(len(PDateEntered)))
        print(PDateEntered)
        print('\n>  Entry Date Loss: ' + str(len(DateLoss)))
        print(DateLoss)
        print('\n>  Entry Date Win: ' + str(len(DateWin)))
        print(DateWin)
        print('\n>  SPL: ' + str(len(SPL)))
        print(SPL)
        print('\n>  SPW: ' + str(len(SPW)))
        print(SPW)
        print('\n>  Sell Loss: ' + str(len(sellLoss)))
        print(sellLoss)
        print('\n>  Sell Profit: ' + str(len(sellProfit)))
        print(sellProfit)
        print('\n>  Trade Win Length:\n%s' % tradeWinLength)
        print('\n>  Trade Loss Length:\n%s' % tradeLossLength)
      

        # Calculating Values for Summary Outputs
        preDefinedRisk = round(reward/risk,1)
        numTradingPeriods = len(self.df)
        numProfits = len(sellProfit)
        numLosses = len(sellLoss)
        numTrades = len(PEnter)
        numTradesCompleted = numProfits + numLosses
        numTradesPercent = round(100*numTradesCompleted/numTradingPeriods,1)
        numProfitsPercentOfTrades = round((100*numProfits/numTradingPeriods),1)
        numLossesPercentOfTrades = round((100*numLosses/numTradingPeriods),1)
        totalProfit = 100*numProfits * reward
        totalLoss = -100*numLosses * risk
        totalNetProfitPercentage = round(totalProfit + totalLoss,1)
        if numTradesCompleted != 0:
            winRate = round(100*numProfits/numTradesCompleted,1)
        else:
            winRate = 0
        avgReturnPerTrade = round(totalNetProfitPercentage/numTradesCompleted,3)
        if len(tradeWinLength) != 0:
            avgNumPeriodsWin = round(sum(tradeWinLength)/len(tradeWinLength),1)
        else: 
            avgNumPeriodsWin = 0
        if len(tradeLossLength) != 0:
            avgNumPeriodsLoss = round(sum(tradeLossLength)/len(tradeLossLength),1)
        else: 
            avgNumPeriodsLoss = 0
        sumTrdPeriodsPercent = round(100*(sum(tradeWinLength)+sum(tradeLossLength))/numTradingPeriods,1)
        buyHoldReturn = round(100*(self.df.loc[len(self.df)-1,'Close'] - self.df.loc[0,'Open']) / self.df.loc[0,'Open'],1)

        # Summary Print Outputs
        print('\n Input Conditions')
        print('>  Reward:Risk = ' + str(preDefinedRisk) + ' : 1')
        print('>  Reward: ' + str(round(100*reward,1)) + '%')
        print('>  Risk: ' + str(round(100*risk,1)) + '%')        

        print('\n Trade Statistics')
        print('>  # of Trading Periods: ' + str(numTradingPeriods))
        print('>  # of Trades Entered: ' + str(numTrades))
        print('>  # Trades Completed: ' + str(numTradesCompleted))
        print('>  Sell for Profit: ' + str(numProfits) + ' (' + str(numProfitsPercentOfTrades) + '%) of trading periods')
        print('>  Sell for Loss: ' + str(numLosses) + ' (' + str(numLossesPercentOfTrades) + '%) of trading periods')
        print('>  Avg # of Periods (W): ' + str(avgNumPeriodsWin))        
        print('>  Avg # of Periods (L): ' + str(avgNumPeriodsLoss))
        print('>  Total # of Trade Periods: ' + str(sumTrdPeriodsPercent) + '%')

        print('\n Totals')
        print('>  Return: ' + str(totalNetProfitPercentage) +'%')
        print('>  Buy/Hold: ' + str(buyHoldReturn) +'%')    
        print('>  Reward:Risk = ' + str(preDefinedRisk) + ' : 1')
        print('>  Win Rate: ' + str(winRate)+'%')
        print('>  Avg Return per Trade: ' + str(avgReturnPerTrade)+'%')

        print('--------------------------------------------------------------------------')
        return [numTradesCompleted,winRate,avgReturnPerTrade, totalNetProfitPercentage, preDefinedRisk,avgNumPeriodsWin,avgNumPeriodsLoss,sumTrdPeriodsPercent]





