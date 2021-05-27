from QTA.UserInput.SetBattingAverage import SetBattingAverage

################################
# Unit Tests (SetBattingAverage)
################################

def test_check_input_value_greater_than_zero():
    userInput = SetBattingAverage(1)
    result = userInput.checkValueInRange()
    assert result > 0

def test_check_input_value_less_than_100():
    userInput = SetBattingAverage(90)
    result = userInput.checkValueInRange()
    assert result == True

def test_check_input_value_for_integer():
    userInput = SetBattingAverage(100)
    result = userInput.checkValueIsInteger()
    assert result == True

