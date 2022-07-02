#! /usr/bin/env python3
import rospy
from smach import State 
from servicesClients.emotionClient import emotionClient
from services.Polly import pollySever
from services.db import dbSever

class Emotion(State):

    def __init__(self):
        State.__init__(self,  outcomes=['2','1','0'], input_keys=['questions','difficulty'], output_keys=['difficulty'])
        self.id = 0
        self.question = ""
        self.anwer = ""
        self.resultOK = "¡Muy bien! Amelia"
        self.resultKO = "Vamos a probar otra vez, ¿Vale?"
        self.count = 0
        self.repeat = False
        
    def execute(self, userdata):
        self.questions = userdata.questions
        self.NUM_QUESTIONS = self.questions
        self.getInfoQuestions(self.questions)
        while self.count < self.NUM_QUESTIONS:
            self.repeat = False
            self.startTalking(self.count, 'slow')
            output = emotionClient(self.answer)
            if output.result == "True":
                pollySever.generarAudio(self.resultOK, 'resultOK.mp3')
                self.count = self.count + 1
                break
            else:
                pollySever.generarAudio(self.resultKO, 'resultKO.mp3')
                if self.repeat == False:
                    self.repeat = True
                    self.startTalking(self.count, 'x-slow')
                    output = emotionClient(self.answer)
                    if output.result == "True":
                        pollySever.generarAudio(self.resultOK, 'resultOK.mp3')
                        self.count = self.count + 1
                        break
                    else:
                        pollySever.generarAudio("No pasa nada, Amelia", 'resultKOFinal.mp3')
                        self.count = self.count + 1
                        break
        self.setResults("True", 0.3)
        pollySever.generarAudio("Vamos a pasar al siguiente ejercicio", 'next.mp3')
        return '0'

    def getInfoQuestions(self, id):
        q = self.getQuestion(id)
        self.question = q['question']
        self.answer = q['answer']
        self.id = q['id']

    def setResults(self, result, time):
        rospy.set_param('emotion', result)
        rospy.set_param('emotionTime', time)

    def getQuestion(self, id):
        q = dbSever.getQuestionFromID(id)
        return q.to_dict()

    def startTalking(self, id, rate):
        nameAudio = 'emotion-' + str(id) + ".mp3"
        pollySever.generarAudio(self.question, nameAudio, rate)
    
        
