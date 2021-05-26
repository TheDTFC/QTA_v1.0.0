class FindGap:
    def __init__(self, bar1_close, bar2_open):
        self.barPrevClose = bar1_close
        self.barCurrOpen = bar2_open

    def gap_Polarity(self):
        """
        Checks the polarity of the bar
        returns: true if green or doji
        """       
        return self.barPrevClose <= self.barCurrOpen
        pass

    def calculate_Gap_Percentage(self):
        return (self.barPrevClose - self.barCurrOpen) / self.barPrevClose
        pass
