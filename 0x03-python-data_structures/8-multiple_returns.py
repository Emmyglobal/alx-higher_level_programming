#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[0] = None
    else:
        answer = (len(sentence), sentence[0])
        return answer
