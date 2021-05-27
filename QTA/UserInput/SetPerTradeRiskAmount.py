class SetPerTradeRiskAmount():

    def __init__(self, riskPercentage, riskDollars, accountValue):
        self.riskPercentage = riskPercentage
        self.riskDollars = riskDollars
        self.accountValue = accountValue

    def convertPercentageToDollars(self):
        if self.riskPercentage == 0:
            return self.riskDollars
        else:            
            return self.riskPercentage * self.accountValue

    def convertDollarsToPercentage(self):
        if self.riskDollars == 0:
            return self.riskPercentage
        else: 
            return self.riskDollars / self.accountValue

    def checkValueInRange(self):
        return 0 < self.riskDollars < self.accountValue
