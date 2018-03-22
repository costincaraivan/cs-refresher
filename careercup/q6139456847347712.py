#  Facebook Interview Question for Software Engineer / Developers
# Microsoft Excel numbers cells as 1...26 and after that AA, AB.... AAA, AAB...ZZZ and so on.
# Given a number, convert it to that format and vice versa.

import logging

logging.basicConfig(level = logging.INFO)


def convertToBase26(input_number):
    output_string = ""
    while input_number != 0:
        digit = (input_number - 1) % 26 + 1
        output_string = chr(ord('A') + digit - 1) + output_string
        input_number = (input_number - digit) // 26
    return output_string


def convertFromBase26(input_number):
    sum = 0
    for character in input_number:
        sum = sum * 26 + ord(character) - ord('A') + 1
    return sum

# Individual checks.
logging.info(convertToBase26(728))
logging.info(convertFromBase26("AAZ"))

# Check of inverse.
logging.info(convertFromBase26(convertToBase26(728)))