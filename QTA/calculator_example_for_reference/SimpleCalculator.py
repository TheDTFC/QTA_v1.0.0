# Test Class for Simple Calculator functions to understand TDD/BDD
class SimpleCalculator:
    def add(self,*args):
        return sum(args)
        pass

    def subtract(self,a,b,c=0):
        return a-b-c
        pass