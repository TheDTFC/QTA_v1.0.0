class SetAccountCapital:
    
    def __init__(self, userAccountCapital):
        self.inputValue = userAccountCapital

    def inputValueGreaterThanZero(self):
        if self.inputValue > 0:
            return True
            pass

    def inputValueIsInteger(self):
        return isinstance(self.inputValue, int)
        pass