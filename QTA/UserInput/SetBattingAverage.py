class SetBattingAverage:
    
    def __init__(self, userBattingAverage):
        self.inputValue = userBattingAverage

    def checkValueInRange(self):
        return 0 < self.inputValue < 100

    def checkValueIsInteger(self):
        return isinstance(self.inputValue, int)