from datetime import datetime
import times
from pytest import raises

def test_given_input():
    """
    A unit test on the times.py file
    """
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = times.compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_no_overlap_input():
    """
    A unit test for non-overlapping periods
    """
    range1 = times.time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    range2 = times.time_range("2010-01-12 11:30:00", "2010-01-12 12:00:00")

    # Raise error when trying to compute overlap period for non-overlapping inputs
    with raises(ValueError):
        times.compute_overlap_time(range1, range2)