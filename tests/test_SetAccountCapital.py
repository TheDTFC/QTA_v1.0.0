from QTA.UserInput.SetAccountCapital import SetAccountCapital
import math as m

from QTA.UserInput.SetAccountCapital import SetAccountCapital

################################
# Unit Tests (SetAccountCapital)
################################

def test_check_input_value_greater_than_zero():
    userInput = SetAccountCapital(1)
    result = userInput.checkValueGreaterThanZero()
    assert result > 0

def test_check_input_value_for_integer():
    userInput = SetAccountCapital(100)
    result = userInput.checkValueIsInteger()
    assert result == True