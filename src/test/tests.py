from ..lib.stats_lib import mean, median, mode, variance, ds
import pytest

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

