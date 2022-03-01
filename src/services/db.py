#! /usr/bin/env python3
# coding=utf-8

import sys
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FirebaseDB:

    def __init__(self):
        self.path = '/home/diana/catkin_ws/src/action-template/src/'
        self.cred = credentials.Certificate( self.path + 'config/jinkobot.json')
        firebase_admin.initialize_app(self.cred)
        self.mainCollection = "patients"
        self.db = firestore.client()

    def changeMainCollectionL(self, newMainCollection):
        self.mainCollection = newMainCollection

    def savePatient(self, data):
        patient_ref = self.db.collection(self.mainCollection).document(data['name'])
        patient_ref.set(
            {
                'name': data['name'],
                'isActive': data['isActive'],
                'sessionCount':  data['sessionCount']
            }
        )

    def saveResults(self, name, data):
        patient_ref = self.db.collection(self.mainCollection).document(name)
        patient_ref.update({u'emotion': firestore.ArrayUnion([data])})

    def getQuestionFromID(self, id):
        ref = self.db.collection(u'questions').document(str(id))
        doc = ref.get()
        return doc

def dbService():
    return  FirebaseDB()

dbSever = dbService()
