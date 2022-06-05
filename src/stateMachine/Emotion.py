#! /usr/bin/env python3
import rospy
from smach import State 
from servicesClients.emotionClient import emotionClient
from services.Polly import pollySever
from services.db import dbSever

class Emotion(State):

    def __init__(self):
        State.__init__(self,  outcomes=['2','1','0'], input_keys=['questions'], output_keys=[1.0, 0.5])
        self.id = 0
        self.question = ""
        self.anwer = ""
        self.resultOK = "¡Muy bien! Amelia"
        self.resultKO = "Vamos a probar otra vez, ¿Vale?"
        self.count = 0
        
    def execute(self, userdata):
        self.questions = userdata.questions
        self.NUM_QUESTIONS = len(self.questions)
        self.getInfoQuestions(self.questions[self.count])
        self.startTalking()
        result = self.startQuestion()
        outcome = result[0]
        timeElapsed = result[1]

        if outcome == "True":
            pollySever.generarAudio(self.resultOK, 'resultOK.mp3')
        else:
            #if self.count == self.NUM_QUESTIONS - 1:
                #pollySever.generarAudio("Vamos a pasar al siguiente ejercicio", 'next.mp3')
            #else:
            pollySever.generarAudio(self.resultKO, 'resultKO.mp3')
            nameAudio = 'emotion-' + str(self.id) + ".mp3"
            pollySever.generarAudio(self.question, nameAudio)
              

        self.setResults(outcome, timeElapsed)
        self.selectNextQuestion()

        if self.count == self.NUM_QUESTIONS:
            print("Se han hecho todas las preguntas")
            return '0'
        return '1'

    def getInfoQuestions(self, id):
        q = self.getQuestion(int(id))
        self.question = q['question']
        self.answer = q['answer']
        self.id = q['id']

    def setResults(self, result, time):
        rospy.set_param('emotion', result)
        rospy.set_param('emotionTime', time)

    def getQuestion(self, id):
        q = dbSever.getQuestionFromID(id)
        return q.to_dict()

    def startTalking(self):
        nameAudio = 'emotion-' + str(self.id) + ".mp3"
        pollySever.generarAudio(self.question, nameAudio)

    def startQuestion(self):
        output = emotionClient(self.answer)
        return [output.result, output.time]
    
    def selectNextQuestion(self):
        self.count = self.count + 1

        

        
