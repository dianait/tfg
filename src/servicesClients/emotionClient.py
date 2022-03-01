#! /usr/bin/env python
import rospy
from jinko_games_message.srv import jinko_games_message, jinko_games_messageRequest

def emotionClient(answer):
    emotionService = rospy.ServiceProxy('/jinko_games_service', jinko_games_message)
    # rospy.loginfo('Conectando con el servicio...')
    # rospy.loginfo('Llamando al servicio /jinko_games_service')
    sos = jinko_games_messageRequest()
    sos.answer = answer
    result = emotionService(sos)
    return str(result.success)

class EmotionResult(object):
    result = ""
    time = 0

def make_EmotionResult(result, time):
    emotionResult = EmotionResult()
    emotionResult.result = result
    emotionResult.time = time
    return emotionResult
