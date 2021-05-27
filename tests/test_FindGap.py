from QTA.Signals.ClassifyBar import ClassifyBar
from QTA.Signals.FindGap import FindGap
import math as m

################################
# Unit Tests (FindGap)
################################

def test_calculate_gap_percentage():
    bars = []
    bars.append(ClassifyBar(4.0, 5.0, 5.35, 3.99, 50000))
    bars.append(ClassifyBar(6.0, 6.4, 7.6, 3.25, 45000))
    
    gap = FindGap(bars[0].close, bars[1].open)

    result = abs(gap.calculate_Gap_Percentage())
    assert m.isclose(result, 0.2)

def test_check_gap_polarity():
    bars = []
    bars.append(ClassifyBar(4.0, 5.0, 5.35, 3.99, 50000))
    bars.append(ClassifyBar(6.0, 6.4, 7.6, 3.25, 45000))
    
    gap = FindGap(bars[0].close, bars[1].open)

    result = gap.gap_Polarity()
    assert result == True

################################
# Unit Tests (ClassifyBar)
################################

def test_check_bar_is_green():
    bar = ClassifyBar(4.0, 5.0, 6.2, 4.0, 50000)
    result = bar.polarity()
    assert result == True


