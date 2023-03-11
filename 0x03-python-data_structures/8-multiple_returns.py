#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        FC = None

    else:
        lenght = len(sentence)
        FC = sentence[0]

    return(lenght, FC)
