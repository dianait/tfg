#! /usr/bin/env python
import rospy
import actionlib # contiene la clase SimpleActionServer
from action_template.msg import actionTemplateAction, actionTemplateFeedback, actionTemplateResult

def callbackAwsPolly(goal):
    r = rospy.Rate(1)
    print(goal.time)
    result = actionTemplateResult() # se construye el mensaje de respuesta
    feedback = actionTemplateFeedback()
    isEven = False
    if goal.time % 2 == 0:
        isEven = True
    
    feedback.currentTime = goal.time * 2
    server.publish_feedback(feedback)
    r.sleep()

    result.success = isEven
    rospy.loginfo('%s: Succeeded')
    server.set_succeeded(result) # se ha enviado el goal OK = True

rospy.init_node('action_template')
server = actionlib.SimpleActionServer('start', actionTemplateAction, callbackAwsPolly, False) # creamos el servidor de la accion
# Los parametros son: nombre del servidor, tipo de la accion, funcion a ejecutar y variable que posibilita el inicio atomatico del servidor
server.start() # iniciamos el servidor
print("Esperando el goal")
rospy.loginfo("Lanzamos el servidor action_template") # Esto solo funciona con Python 3
rospy.spin() # el server queda a la espera de recibir el goal


