#! /usr/bin/env python3
from smach import StateMachine
from stateMachine.Emotion import Emotion 
from stateMachine.Orientation import Orientation
from stateMachine.Grettings import Grettings
from stateMachine.Results import Results

class StateMachineClass:
    def __init__(self, name, questions):
        self.sm = StateMachine(outcomes=['succeeded','aborted'])
        self.sm.userdata.name = name
        self.sm.userdata.questions = questions
        with self.sm:
            StateMachine.add('Grettings', Grettings(), 
            transitions={'1':'Emotion', '0': 'succeeded', '2': 'aborted'}, remapping={'input':'time','output':'input'})
            StateMachine.add('Emotion', Emotion(), 
            transitions={'1':'Emotion', '0': 'Orientation', '2': 'aborted'}, remapping={'input':'time','output':'input'})
            StateMachine.add('Orientation', Orientation(), 
            transitions={'1':'Results', '0': 'succeeded', '2': 'aborted'}, remapping={'input':'time','output':'input'})
            StateMachine.add('Results', Results(), 
            transitions={'1':'Emotion', '0': 'succeeded', '2': 'aborted'}, remapping={'input':'time','output':'input'})

    def execute(self):
        self.sm.execute()

    
