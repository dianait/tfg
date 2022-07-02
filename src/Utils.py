#! /usr/bin/env python3
from mimetypes import init
import rospy

class Utils:

    def __init__(self):
        print("Utils initialized")

    def getParams(self):
        name = rospy.get_param('name')
        questions = rospy.get_param('questions')
        difficulty = rospy.get_param('difficulty')
        return {'name': name, 'questions': questions, 'difficulty': difficulty}

    def isInfoCorrect(self, userdata):
        name = userdata.name
        questions = userdata.questions
        difficulty = userdata.difficulty
        if not name or not questions or not difficulty: 
            return False
        return True

    def saveData(self, userdata):
        name = userdata.name
        questions = userdata.questions
        difficulty = userdata.difficulty
        rospy.set_param('name', name)
        rospy.set_param('questions', questions)
        rospy.set_param('difficulty', difficulty)
