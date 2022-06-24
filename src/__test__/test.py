#!/usr/bin/env python
PKG = 'action_template'
import unittest
from test import support

class MyTestCase1(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    def setUp(self):
        print(" code to execute in preparation for tests")

    def tearDown(self):
        print("code to execute to clean up after tests")

    def test_feature_one(self):
        print("testing code")

    def test_feature_two(self):
        print("testing code")

class MyTestCase2(unittest.TestCase):
    print("same structure as MyTestCase1")
    print("... more test classes ...")

if __name__ == '__main__':
    unittest.main()