from datetime import datetime
from times import time_range, compute_overlap_time
import pytest
from pytest import raises

@pytest.mark.parametrize("range1, range2, expected", 
[
# General overlap case
(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
(time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)),
[("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]),   

# Both ranges with multiple periods
(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
 time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
 [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]),

# Common start end time
(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
 time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00", 2, 60),
 []),

# No-overlap
(time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00"),
 time_range("2010-01-12 11:30:00", "2010-01-12 12:00:00"),
 [])])

def test_compute_overlap_time(range1, range2, expected):
    """
    Parametrised unit for for compute_overlap_time()
    """
    result = compute_overlap_time(range1,range2)
    assert result == expected

def test_valid_time_range():
    """
    Negative test: end time must be after start time. Otherwise raise error
    """
    with raises(ValueError):
        range = time_range("2010-01-12 11:00:00", "2010-01-12 10:00:00")
