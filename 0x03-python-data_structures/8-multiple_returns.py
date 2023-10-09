#!/usr/bin/python3
"""
function that returns a tuple with the length of a string
and its first character.
"""


def multiple_returns(sentence):
    if not sentence:
        x = None
        _len = 0
    else:
        _len = len(sentence)
        x = sentence[0]

    return _len, x
