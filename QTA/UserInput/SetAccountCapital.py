class SetAccountCapital:
    
    def __init__(self, userAccountCapital):
        self.capital = userAccountCapital

    def checkValueGreaterThanZero(self):
        return self.capital > 0

    def checkValueIsInteger(self):
        return isinstance(self.capital, int)