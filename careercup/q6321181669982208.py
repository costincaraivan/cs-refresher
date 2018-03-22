# Facebook Interview Question for Software Engineer / Developers
# Given a number N, write a program that returns all possible
# combinations of numbers that add up to N, as lists. (Exclude N + 0 = N)
# For example, if N = 4 return {{1,1,1,1},{1,1,2},{2,2},{1,3}}

import logging

logging.basicConfig(level = logging.INFO)


def integer_partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in integer_partition(number - x):
            combination = tuple(sorted((x, ) + y))
            answer.add(combination)
            logging.info("number: {} x: {} y: {} combination: {}".format(
                number, x, y, combination))
    return answer

logging.info(integer_partition(6))