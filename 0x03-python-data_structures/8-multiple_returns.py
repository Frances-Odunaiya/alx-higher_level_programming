#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return(0, "None")
    count = len(sentence)
    first_char = sentence[0]
    return(count, first_char)
