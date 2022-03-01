#! /usr/bin/env python
import rospy
from jinko_service_msg.srv import jinko_service_msg, jinko_service_msgRequest 

def orientationClient(coordx, coordy):
    orientationServer = rospy.ServiceProxy('/jinko_navigation', jinko_service_msg)
    rospy.loginfo('Llamando al servicio /jinko_navigation')
    message = jinko_service_msgRequest()
    message.destino = 0
    message.coordenadaX = coordx 
    message.coordenadaY = coordy
    result = orientationServer(message)
    return result

