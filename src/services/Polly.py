import boto3
import pygame
import time
import os
from config.AWS import AWSsesion

class Polly:
    def __init__(self):
        """This is the contructor of Polly class

        Args:
            awsSession (array): Credential of Amazon Web Services
            rutaFicheroPistas (string): Path where we save the files
        """                  
        self.baseURL = "/home/diana/catkin_ws/src/action-template/src/audios/"
        self.awsSession = AWSsesion
        # Propiedades configurables del servicio
        # Ruta donde se guardaran las pistas
        self.rutaFicheroPistas = "/audios" 
        
        # Voz que se usara por defecto 
        self.vozId = 'Lucia'
        # Formato en el que se genera la pista de audio pr defecto
        self.outputFormat = "ogg_vorbis"
        
        # Creamos la sesion de AWS
        session = boto3.Session( 
                        aws_access_key_id= self.awsSession[0], 
                        aws_secret_access_key= self.awsSession[1],
                        aws_session_token= self.awsSession[2],
                        region_name='us-east-1')

        # Accedemos al servicio Polly
        self.polly_client = session.client('polly')
    
    
    def configurarVoz(self, vozId, outputFormat):
        """This is a method of Polly class

        Args:
            vozId (string): The name of the voice
            outputFormat (string): Format of the audio fila
        """        
        self.vozId = vozId
        self.outputFormat = outputFormat
        
    # Metodo que genera una pista de audio a partir de un texto
    def generarAudio(self, texto, nombreArchivo, rate = "slow"):
        """This is a method of Polly class

        Args:
            texto (string): Text to reproduce
            nombreArchivo (string): The name of file tha we can generate
        """        
        
        if not self.checkIfAudioExist(nombreArchivo):
            response = self.polly_client.synthesize_speech(
                    VoiceId=self.vozId,
                    Engine="neural",
                    TextType="ssml",
                    OutputFormat=self.outputFormat, 
                    Text = "<prosody rate='%s'> %s </prosody>" % (rate,texto))

            archivo = self.baseURL + nombreArchivo
        
            print(archivo)
            file = open(archivo, 'wb')
            file.write(response['AudioStream'].read())
            file.close()
        
        self.reproducirAudio(nombreArchivo)
    
    # Metodo que reproduce la pista
    def reproducirAudio(self,nombreArchivo):
        """This is a method of Polly class

        Args:
            nombreArchivo (string): Name of the file that we can play
        """        
        archivo = self.baseURL + nombreArchivo # Ruta donde se encuentra el archivo
        
        #  Uso de la libreria pygame para la reporduccion de audio
        pygame.init()
        sound = pygame.mixer.Sound(archivo) # Guardamos el audio en una variable
        sound.play() # Reproduccion del audio
        time.sleep(sound.get_length() + 0.5) # 
        pygame.quit()
    
    # Metodo que reproduce la pista
    def borrarAudio(self,nombreArchivo):
        """This is a method of Polly class

        Args:
            nombreArchivo (string): Name of file that we can delete
        """        
        
        archivo = self.rutaFicheroPistas+"/"+nombreArchivo # Ruta donde se encuentra el archivo
        os.remove(archivo) # Borrar archivo

    def checkIfAudioExist(self, nameAudio):
        for f in os.walk(self.baseURL):
            for files in f:
                if files == nameAudio:
                    return True
                return False

    def generateSSML(self):
        response = self.polly_client.synthesize_speech(
                    VoiceId=self.vozId,
                    Engine="neural",
                    TextType="ssml",
                    OutputFormat=self.outputFormat, 
                    Text = "<prosody rate='x-slow'>Hola que tal?</prosody>")

        archivo = self.baseURL + "test"
        
        print(archivo)
        file = open(archivo, 'wb')
        file.write(response['AudioStream'].read())
        file.close()
        
        self.reproducirAudio("test")

def polly():
    return Polly()

pollySever = polly()