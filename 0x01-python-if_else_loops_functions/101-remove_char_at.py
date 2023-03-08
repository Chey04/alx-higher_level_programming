#!/usr/bin/python3
def remove_char_at(str, n):
     if index < 0 or index >= len(string):
        # Index is out of range, return the original string.
        return string

    # Split the string into two parts: before the index and after the index.
    before = string[:index]
    after = string[index + 1:]

    # Concatenate the two parts and return the result.
    return before + after

