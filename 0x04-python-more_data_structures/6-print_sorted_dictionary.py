#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sortedKey = sorted(a_dictionary.keys())
    sortedDict = {key:a_dictionary[key] for key in sortedKey}

    return (sortedDict)
