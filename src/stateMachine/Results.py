#! /usr/bin/env python3
import rospy
from smach import State
from services.Polly import pollySever
from services.db import dbSever
from datetime import datetime

class Results(State):
    def __init__(self):
        State.__init__(self,  outcomes=['2','1','0'], input_keys=['name'], output_keys=[])

    def execute(self, userdata):
        self.debug(userdata)
        # self.testSavePatient()
        # self.testSaveResults()
        return '0'

    def debug(self, userdata):
        message = "Hemos terminado, " + userdata.name + ". Lo has hecho muy bien. ¡Hasta la próxima!"
        nameAudio = "results-" + userdata.name + ".mp3"
        pollySever.generarAudio(message, nameAudio)
        name = rospy.get_param('name')
        emotion = rospy.get_param('emotion')
        emotionTime = rospy.get_param('emotionTime')
        orientation = rospy.get_param('orientation')
        orientationTime = rospy.get_param('orientationTime')
        print("---------------------------------------------------")
        print("--------RESUME DE LA SESIÓN de "+ name +"----------")
        print("Emotion result " + str(emotion) + " in " + str(emotionTime) + " s")
        print("Orientation result " + orientation + " in " + str(orientationTime) + " s")
        print("¡Muy bien! Hemos terminado")
        print("---------------------------------------------------")

    def testSavePatient(self):
        name = rospy.get_param('name')
        patient = {}
        patient['name'] = name
        patient['isActive'] = True
        patient['sessionCount'] = 1
        dbSever.savePatient(patient)

    def testSaveResults(self):
        totalQuestions = 1
        ok = ""
        name = rospy.get_param('name')
        emotion = rospy.get_param('emotion')
        emotionTime = rospy.get_param('emotionTime')
        now = datetime.now()

        if emotion == "True":
            ok = "1/" + str(totalQuestions)
        else:
            ok = "0/" + str(totalQuestions)

        results = {}
        results['date'] = datetime.timestamp(now)
        # results['ko'] = ko
        results['latence'] = -12
        results['ok'] = ok
        results['omision'] = '0/3'
        results['totalTime'] = emotionTime
        dbSever.saveResults(name, results)



