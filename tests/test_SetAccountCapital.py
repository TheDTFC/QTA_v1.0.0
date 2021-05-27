from QTA.UserInput.SetAccountCapital import SetAccountCapital
import math as m

################################
# Unit Tests (SetAccountCapital)
################################

def test_check_for_input_value_greater_than_zero():
    userInput = SetAccountCapital(1)
    result = userInput.inputValueGreaterThanZero()
    assert result > 0

def test_check_for_integer_input_value():
    userInput = SetAccountCapital(100.0)
    result = userInput.inputValueIsInteger()
    assert result == True