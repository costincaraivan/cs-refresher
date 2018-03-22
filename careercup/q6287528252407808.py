# https://careercup.com/question?id=6287528252407808
# A k-palindrome is a string which transforms into a palindrome on removing at most k characters.
# Given a string S, and an interger K, print "YES" if S is a k-palindrome; otherwise print "NO".
# Constraints:
# S has at most 20,000 characters.
# 0<=k<=30
# Sample Test Case#1:
# Input - abxa 1
# Output - YES
# Sample Test Case#2:
# Input - abdxa 1
# Output - No

# import unittest
import logging

logging.basicConfig(level = logging.INFO)


# TODO: Not solved yet, moving on to other problems for now.
def k_palindrome(input_string, k):
    mid_point = len(input_string) // 2
    string1 = input_string[:mid_point]
    string2 = input_string[mid_point:][::-1]
    n = len(string1)
    logging.info("string1: {}, string2: {}".format(string1, string2))

    edit_distance = [ [ 0 ] * n ] * n

    for i in range(1, n):
        start = max(1, i - k)
        end = min(i + k, n)
        for j in range(start, end):
            if string1[i - 1] == string2[j - 1]:
                edit_distance[i][j] = edit_distance[i - 1][j - 1]

            edit_distance[i][j] = min(edit_distance[i][j], 1 + edit_distance[i][j - 1])
            edit_distance[i][j] = min(edit_distance[i][j], 1 + edit_distance[i - 1][j])

    logging.info(edit_distance)

    return edit_distance[n - 1][n - 1]


logging.info(k_palindrome("abba", 1))