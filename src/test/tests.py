from ..lib.stats_lib import mean, median, mode, variance, ds
import pytest
import math

def testMean():
    assert mean([1, 2, 3, 4]) == 2.5
    assert mean([10, 20, 30]) == 20
    with pytest.raises(ValueError):
        mean([])

def testMedian():
    assert median([1, 3, 2]) == 2
    assert median([1, 2, 3, 4]) == 2.5
    with pytest.raises(ValueError):
        median([])

def testMode():
    assert mode([1, 1, 2, 3]) == 1
    assert set(mode([1, 2, 2, 3, 3])) == {2, 3}
    with pytest.raises(ValueError):
        mode([1, 2, 3])  

def testVariance():
    assert math.isclose(variance([1, 2, 3, 4, 5]), 2.0)
    assert variance([5, 5, 5]) == 0
    with pytest.raises(ValueError):
        variance([])