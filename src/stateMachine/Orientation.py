#! /usr/bin/env python3
import rospy
from smach import State
from time import time
from servicesClients.orientationClient import orientationClient

class Orientation(State):
    def __init__(self):
        State.__init__(self,  outcomes=['2','1','0'], input_keys=[], output_keys=[])

    def execute(self, userdata):

        if not userdata: return '2'
        coordx = 1.0
        coordy = 3.0

        print("Estamos en el estado Orientation")
        rospy.set_param('orientation', '3/4')
        # coordx = userdata.coordx
        # coordy = userdata.coordy

        start = time()
        # orientationClient(coordx, coordy)
        end = time()

        timeElapsed = round((end - start),2)
        rospy.set_param('orientationTime', timeElapsed)
        return '1'
        