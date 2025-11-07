from datetime import datetime
from times import time_range, compute_overlap_time
from pytest import raises

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_given_input():
    """
    A unit test on the times.py file
    """
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 0)
    short = time_range("2010-01-12 11:00:00", "2010-01-12 14:00:00", 3, 0)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 11:00:00', '2010-01-12 12:00:00')]
    assert result == expected

def test_no_overlap_input():
    """
    A unit test for non-overlapping periods
    """
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    range2 = time_range("2010-01-12 11:30:00", "2010-01-12 12:00:00")

    # Raise error when trying to compute overlap period for non-overlapping inputs
    result = compute_overlap_time(range1, range2)
    expected = []
    assert result == expected

def test_common_start_end_time():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00", 2, 60)
    expected = []
    assert compute_overlap_time(large, short) == expected

def test_valid_time_range():
    with raises(ValueError):
        range = time_range("2010-01-12 11:00:00", "2010-01-12 10:00:00")
