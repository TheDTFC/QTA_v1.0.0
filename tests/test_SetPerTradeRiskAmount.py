from QTA.UserInput.SetPerTradeRiskAmount import SetPerTradeRiskAmount

################################
# Unit Tests (SetPerTradeRiskAmount)
################################

def test_convert_risk_percentage_to_dollars():
    riskValue = SetPerTradeRiskAmount(0.01,0,1000)
    result = riskValue.convertPercentageToDollars()
    assert result == 10

def test_convert_risk_dollars_to_percentage():
    riskValue = SetPerTradeRiskAmount(0,100,1000)
    result = riskValue.convertDollarsToPercentage()
    assert result == 0.1

def test_check_risk_dollars_within_range():
    riskValue = SetPerTradeRiskAmount(0,100,1000)
    result = riskValue.checkValueInRange()
    assert result == True

