#!/usr/bin/python3
'''writes string to textfile'''


def write_file(filename="", text=""):
    '''function to write string to textfile

    Args:
        filename(str): file to write to
        text(str): string to write
    Return:
        number of characters written
    '''
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
