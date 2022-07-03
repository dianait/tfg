#!/usr/bin/env python3
PKG = 'action_template'
import sys
import unittest
import rostest
import rospy
from jinko_games_message.srv import jinko_games_message, jinko_games_messageRequest

def emotionClient(answer):
    emotionService = rospy.ServiceProxy('/jinko_games_service', jinko_games_message)
    # rospy.loginfo('Conectando con el servicio...')
    # rospy.loginfo('Llamando al servicio /jinko_games_service')
    sos = jinko_games_messageRequest()
    sos.answer = answer
    result = emotionService(sos)
    return make_EmotionResult(str(result.success), result.timeElapsed)

class EmotionResult(object):
    result = ""
    time = ""

def make_EmotionResult(result, time):
    emotionResult = EmotionResult()
    emotionResult.result = result
    emotionResult.time = time
    return emotionResult

class ServicesTests(unittest.TestCase):

    def setUp(self):
        self.userdata = {'name': '', 'questions': 2, 'difficulty': 'facil'}

    def test_call_emotion_service(self):
        outcome = emotionClient("triste2")
        self.assertEquals(outcome.result, 'False')
        self.assertEquals(outcome.time, '0.0')

if __name__ == '__main__':
    rostest.rosrun(PKG, 'services_tests', ServicesTests)
PKG = 'action_template'
import sys
import unittest
import rostest
import rospy
from jinko_games_message.srv import jinko_games_message, jinko_games_messageRequest

def emotionClient(answer):
    emotionService = rospy.ServiceProxy('/jinko_games_service', jinko_games_message)
    # rospy.loginfo('Conectando con el servicio...')
    # rospy.loginfo('Llamando al servicio /jinko_games_service')
    sos = jinko_games_messageRequest()
    sos.answer = answer
    result = emotionService(sos)
    return make_EmotionResult(str(result.success), result.timeElapsed)

class EmotionResult(object):
    result = ""
    time = ""

def make_EmotionResult(result, time):
    emotionResult = EmotionResult()
    emotionResult.result = result
    emotionResult.time = time
    return emotionResult

class ServicesTests(unittest.TestCase):

    def setUp(self):
        self.userdata = {'name': '', 'questions': 2, 'difficulty': 'facil'}

    def test_call_emotion_service(self):
        outcome = emotionClient("triste2")
        self.assertEquals(outcome.result, 'False')
        self.assertEquals(outcome.time, '0.0')

if __name__ == '__main__':
    rostest.rosrun(PKG, 'services_tests', ServicesTests)
