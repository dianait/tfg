#!/usr/bin/env python
PKG = 'action_template'
import sys  
import unittest
import rospy
sys.path.append('/home/diana/catkin_ws/src/action-template/src')     
from Utils import Utils

class UtilTests(unittest.TestCase):

    def setUp(self):
        self.utils = Utils()
        self.userdata = {'name': 'Jinko', 'questions': 2, 'difficulty': 'facil'}

    def test_data_correct(self):
        outcome = self.utils.isInfoCorrect( self.userdata )
        self.assertEquals(outcome, True)

    def test_save_data_correct(self):
        self.utils.saveData( self.userdata)
        outcome = self.utils.getParams()
        self.assertEquals(outcome, self.userdata)

if __name__ == '__main__':
    import rosunit
    rospy.init_node("test")
    rosunit.unitrun(PKG, 'MyTestCase1', UtilTests)
