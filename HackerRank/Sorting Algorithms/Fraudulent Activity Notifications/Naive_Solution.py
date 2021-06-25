from statistics import median
#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d


def activityNotifications(expenditure, d):
    # Write your code here
    notifications = 0
    remaining_days = len(expenditure) - d
    median_value = 0
    medians = []
    for index in range(remaining_days):
        ## calculate median
        median_value = median(expenditure[index:d])
        medians.append(median_value)
        if 2*median_value <= (expenditure[d]):
            notifications += 1
        d += 1
    return notifications