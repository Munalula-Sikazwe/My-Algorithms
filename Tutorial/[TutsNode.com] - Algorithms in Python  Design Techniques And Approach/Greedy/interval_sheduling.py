intervals = [
    [0, 3],
    [0, 15],
    [5, 10],
    [7, 12],
    [11, 16],
    [12, 14],
    [16, 20],

]


def interval_sheduling(intervals):
    intervals.sort(key=lambda i: i[1])

    last_finish_time = float("-inf")
    optimal_intervals = []
    for interval in intervals:
        start = interval[0]
        if start > last_finish_time:
            end = interval[1]
            optimal_intervals.append(interval)
            last_finish_time = end

    return optimal_intervals




