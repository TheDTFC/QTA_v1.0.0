
from numpy import NaN, result_type


class SetEntryExits:
    def __init__(self, df_total):
        self.df = df_total

    def setPriceEntry(self):
        return self.df["Buy"] * self.df["Close"].shift(1)

    def setPriceLimitTarget(self, reward):
        return self.df["PriceEntry"] * (1 + reward)

    def setPriceStopLoss(self, risk):
        return self.df["PriceEntry"] * (1 - risk)

    def checkSellSignal(self):
        result = self.df["Buy"]
        #print(result)
        return result

    def checkTradeEntered(self):
        #workaround to get original True/False to be swapped
        result = self.df["Buy"]
        result = result.replace(True, 5)
        result = result.replace(False, 3)
        result = result.replace(5, False)
        result = result.replace(3, True)

        result = self.df["Buy"] & result.shift(1).astype(bool)        
        return result

    def updatePriceEntry(self):
        result = self.df["tradeEntered"]
        
        result = result.replace(True, 2)
        result = result.replace(False, NaN)
        result = result * self.df["PriceEntry"] / 2
        result.fillna(method='ffill', inplace=True)   
        return result

