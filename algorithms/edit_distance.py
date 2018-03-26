# import unittest
import logging
from timeit import timeit

logging.basicConfig(level=logging.INFO)


def memoize(function):
    cache = {}

    def memo(*args):
        if args not in cache:
            cache[args] = function(*args)
        return cache[args]

    return memo


@memoize
def edit_distance_recursive(string1, string2):
    if string1 == "":
        return len(string2)
    if string2 == "":
        return len(string1)

    if string1[-1] == string2[-1]:
        cost = 0
    else:
        cost = 1

    return min(
        edit_distance_recursive(string1[:-1], string2) + 1,
        edit_distance_recursive(string1, string2[:-1]) + 1,
        edit_distance_recursive(string1[:-1], string2[:-1]) + cost
    )


logging.info(edit_distance_recursive("intention", "execution"))
logging.info(edit_distance_recursive("jackrabbits", "jackhammer"))
logging.info(edit_distance_recursive("ie", "e"))


def edit_distance_iterative(string1, string2):
    rows = len(string1)
    columns = len(string2)
    if rows == 0:
        return columns
    if columns == 0:
        return rows

    # Initalize 2D array.
    edit_distances = [[0] * columns for i in range(rows)]

    for row in range(rows):
        edit_distances[row][0] = row
    for column in range(columns):
        edit_distances[0][column] = column

    for column in range(1, columns):
        for row in range(1, rows):
            if string1[row - 1] == string2[column - 1]:
                cost = 0
            else:
                cost = 1

            edit_distances[row][column] = min(
                edit_distances[row - 1][column] + 1,
                edit_distances[row][column - 1] + 1,
                edit_distances[row - 1][column - 1] + cost
            )

    # for row in range(rows):
    #    logging.info(edit_distances[row])

    return edit_distances[row][column]


logging.info(edit_distance_iterative("intention", "execution"))
logging.info(edit_distance_iterative("jackrabbits", "jackhammer"))
logging.info(edit_distance_iterative("ie", "e"))

logging.info(timeit('edit_distance_recursive("intention", "execution")',
                    setup='from __main__ import edit_distance_recursive', number=100))
logging.info(timeit('edit_distance_iterative("intention", "execution")',
                    setup='from __main__ import edit_distance_iterative', number=100))