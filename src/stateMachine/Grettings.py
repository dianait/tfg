#! /usr/bin/env python3
from smach import State
from services.Polly import pollySever
from Utils import Utils

class Grettings(State):
    def __init__(self):
        State.__init__(self, outcomes=['2','1','0'], input_keys=['name', 'questions','difficulty'], output_keys=['questions', 'difficulty'])
        self.utils = Utils()

    def execute(self, userdata):
        if not userdata.name:
            return '2'

        self.utils.saveData(userdata)
        self.startTalking(userdata)
        return '1'

    def startTalking(self, userdata):
        message = "Hola, "+ str(userdata.name) + ", soy Jinko. Vamos a empezar..."
        nameAudio = 'grettings-' + userdata.name + ".mp3"
        pollySever.generarAudio(message, nameAudio)
