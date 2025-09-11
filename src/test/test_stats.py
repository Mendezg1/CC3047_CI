import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lib.stats_lib import mean, median, mode, variance, sd
import pytest
import math


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5
    assert mean([10, 20, 30]) == 20
    with pytest.raises(ValueError):
        mean([])

def test_median():
    assert median([1, 3, 2]) == 2
    assert median([1, 2, 3, 4]) == 2.5
    with pytest.raises(ValueError):
        median([])

def test_mode():
    assert mode([1, 1, 2, 3]) == 1
    assert set(mode([1, 2, 2, 3, 3])) == {2, 3}
    with pytest.raises(ValueError):
        mode([1, 2, 3])  

def test_variance():
    assert math.isclose(variance([1, 2, 3, 4, 5]), 2.0)
    assert variance([5, 5, 5]) == 0
    with pytest.raises(ValueError):
        variance([])

def test_sd():
    assert math.isclose(sd([1, 2, 3, 4, 5]), math.sqrt(2.0))
    assert sd([5, 5, 5]) == 0

def run_tests():
    pytest.main()

if __name__ == "__main__":
    run_tests()
