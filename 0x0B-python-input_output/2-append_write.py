#!/usr/bin/python3
'''appends string to textfile'''


def append_write(filename="", text=""):
    '''function to append string to textfile

    Args:
        filename(str): file to write to
        text(str): string to append
    Return:
        number of characters appended
    '''
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))

