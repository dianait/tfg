#! /usr/bin/env python3
import rospy
import actionlib 
from action_template.msg import actionTemplateAction, actionTemplateResult
from stateMachine.stateMachine import StateMachineClass

def start(goal):
    name = goal.name
    questions = goal.questions
    difficulty = goal.difficulty
    sm = StateMachineClass(name, questions, difficulty)
    sm.execute()
    result = actionTemplateResult()
    result.success = True
    # rospy.loginfo('%s: Succeeded')
    server.set_succeeded(result) 

rospy.init_node('jinko')
server = actionlib.SimpleActionServer('jinkoAction', actionTemplateAction, start, False) 
server.start()
print("Esperando el goal")
rospy.loginfo("Lanzamos el servidor action_template") 
rospy.spin() 

# feedback = actionTemplateFeedback()
# feedback.currentTime = goal.time * 2
# server.publish_feedback(feedback)