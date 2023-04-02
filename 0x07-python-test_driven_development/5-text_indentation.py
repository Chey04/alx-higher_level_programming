#!/usr/bin/python3

def text_indentation(text):
    """
    This function seperates a text string at . ? :

    Args:
    text(str): body of text

    Returns:
    split body of text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = [".", "?", ":"]
    lines = []
    line_start = 0
    for i in range(len(text)):
        if text[i] in punctuations:
            lines.append(text[line_start:i+1].strip())
            line_start = i+1

    lines.append(text[line_start:].strip())
    for line in lines:
        print(line)
        print()
