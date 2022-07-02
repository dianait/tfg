#! /usr/bin/env python3
import rospy
from smach import State
from time import time
from servicesClients.orientationClient import orientationClient
from services.Polly import pollySever
class Orientation(State):
    def __init__(self):
        State.__init__(self,  outcomes=['2','1','0'], input_keys=['difficulty'], output_keys=[])

    def execute(self, userdata):
        if not userdata: return '2'
        difficulty = userdata.difficulty
        if difficulty == "facil":
            coordx = 4.3
            coordy = -0.12
            self.initMovement(coordx, coordy)

        else:
            self.startTalking(nameAudio = "orientation.mp3", 
            text="Muy bien Amelia. Quiero que me sigas despacio ¿Estás preparada?")
            start = time()
            orientationClient(1.19, -0.47)
            self.startTalking(nameAudio = "orientation2.mp3", 
            text="¡Estupendo! Vamos a cambiar de dirección, Amelia")
            orientationClient(2.38, 1.05)
            self.startTalking(nameAudio = "orientation3.mp3", 
            text="Ya nos queda muy poco. ¡Sígueme, Amelia!")
            orientationClient(3.67, -0.55)
            end = time()
            self.saveTime(start, end)
        return '1'

    def initMovement(self, coordx, coordy):
        self.startTalking(nameAudio = "orientation.mp3", 
        text="Muy bien Amelia. Quiero que me sigas despacio ¿Estás preparada?")
        start = time()
        orientationClient(coordx, coordy)
        end = time()
        self.saveTime(start, end)

    def saveTime(self, start, end):
        timeElapsed = round((end - start),2)
        rospy.set_param('orientationTime', timeElapsed)

    def startTalking(self, nameAudio, text):
        pollySever.generarAudio(text, nameAudio, "slow")
    

        