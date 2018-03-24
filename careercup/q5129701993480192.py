# Facebook Interview Question for Software Engineer / Developers
# Given an array of ages (integers) sorted lowest to highest, output the number of occurrences for each age.
# For instance:  [8,8,8,9,9,11,15,16,16,16] should output something like:
# 8: 3
# 9: 2
# 11: 1
# 15: 1
# 16: 3
# This should be done in less than O(n).

import logging

logging.basicConfig(level = logging.INFO)


def age_histogram(ages):
    # Make an array with just the ages in the original array.
    histogram = dict.fromkeys(ages, 0)
    count_ages(ages, 0, len(ages) - 1, histogram)
    return histogram


def count_ages(ages, start, end, histogram):
    # logging.info("start: {}, end: {}, histogram: {}".format(start, end, histogram))
    if(ages[start] == ages[end]):
        histogram[ages[start]] += end - start + 1
    else:
        partition_point = (start + end) // 2
        count_ages(ages, start, partition_point, histogram)
        count_ages(ages, partition_point + 1, end, histogram)

age_array = [ 8, 8, 8, 9, 9, 11, 15, 16, 16, 16 ]
logging.info(age_histogram(age_array))