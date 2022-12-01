def count_overlapping(list_intervals, point):
    return sum(min(x) <= point <= max(x) for x in list_intervals)
