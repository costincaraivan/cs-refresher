# https://careercup.com/question?id=19300678
# If a = 1, b = 2, c = 3,..,z = 26. Given a string, find all possible codes
# that string can generate. Give a count as well as print the strings.
# For example: Input: "1123".
# You need to generate all valid alphabet codes from this string.
# Output List
#    aabc //a = 1, a = 1, b = 2, c = 3
#    kbc // since k is 11, b = 2, c= 3
#    alc // a = 1, l = 12, c = 3
#    aaw // a= 1, a =1, w= 23
#    kw // k = 11, w = 23

import unittest
import logging

logging.basicConfig(level = logging.INFO)


def memoize(function):
    cache = {}

    def memo(key):
        if key not in cache:
            cache[key] = function(key)
        return cache[key]
    return memo


def decode_integer_string(input_string):
    @memoize
    def get_decoding_branches(input_string):
        logging.info(input_string)
        if not input_string or len(input_string) == 1:
            return 0
        if input_string[0:2] <= '26':
            if '0' not in input_string[1:3]:
                return 1 + get_decoding_branches(input_string[1:]) + get_decoding_branches(input_string[2:])
            else:
                return get_decoding_branches(input_string[2:])
        else:
            return get_decoding_branches(input_string[1:])
    return 1 + get_decoding_branches(input_string)


class TestDecodeIntegerString(unittest.TestCase):
    def test_decode_integer_string(self):
        logging.info(decode_integer_string("1123"))


if __name__ == "__main__":
    unittest.main(verbosity = 2)