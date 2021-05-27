from QTA.UserInput.SetRewardToRiskRatio import SetRewardToRiskRatio

################################
# Unit Tests (SetRewardToRiskRatio)
################################

def test_check_input_value_greater_than_zero():
    userInput = SetRewardToRiskRatio(1.5)
    result = userInput.checkValueInRange()
    assert result > 0