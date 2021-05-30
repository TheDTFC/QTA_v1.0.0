class FindGap:
    def __init__(self, df_open, df_close):
        self.barCurrClose = df_close
        self.barNextOpen = df_open

    def gap_Polarity(self):
        
        #Checks the polarity of the bar
        #returns: true if green or doji
               
        return self.barCurrClose.shift(1) <= self.barNextOpen
        pass

    def gap_Value(self):
        
        #Checks the polarity of the bar
        #returns: true if green or doji
               
        return  self.barNextOpen - self.barCurrClose.shift(1)
        pass

    def gap_Percentage(self):
        return (self.barNextOpen - self.barCurrClose.shift(1)) / self.barCurrClose.shift(1) * 100
        pass
