#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_val(self):
        NumList = [1, 3, 6, 9]
        ExpectedResult = 9
        self.assertEqual(max_integer(NumList), ExpectedResult)

    def TestOrderedList(self):
        numList = [4, 5, 6, 8]
        self.assertEqual(max_integer(numList), 8)

    def TestFloat(self):
        floats = [9.8, 66.4, 4.3, 23.2]
        self.assertEqual(max_integer(floats), 66.4)

    def TestFloatInts(self):
        floats_ints = [2.5, 8, 4.9, 5]
        self.assertEqual(max_integer(floats_ints), 8)

    def TestMaxBegin(self):
        Numlist = [98, 4, 3, 7, 9]
        self.assertEqual(max_integer(Numlist), 98)

    def TestSingle(self):
        Single = [4]
        self.assertEqual(max_integer(Single), 7)

    def TestEmpty(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def TestString(self):
        pythonString = "Riverdale"
        self.assertEqual(max_integer(pythonString), 'r')

    def TestStringList(self):
        strList = ["Alice", "in", "Wonderland"]
        self.assertEqual(max_integer(strList), "in")

    def TestEmptyString(self):
        self.assertEqual(max_integer(""), None)

    if __name__ == '__main__':
        unittest.main()




