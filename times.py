import datetime
from pytest import raises

def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    """
    Calculate duration between two times and create a list of interval tuples
    """
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]

def compute_overlap_time(range1, range2):
    """
    Finds all overlapping periods between 2 set of time ranges
    """
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            if low < high:
            # Add test to check whether given time ranges actually overlap
            # if low >= high:
            #     raise ValueError(f"Non-overlapping time ranges: {(start1, end1)} and {(start2, end2)}")
                overlap_time.append((low, high))
    return overlap_time

large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 0)
short = time_range("2010-01-12 11:00:00", "2010-01-12 14:00:00", 3, 0)
print(compute_overlap_time(large, short))
