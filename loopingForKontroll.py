import os

class Looping:

    def __init__(self, boole, name, commandName):
     self.isRunning = boole
     self.name = name 
     self.command = commandName 


    def runForever(self):
       while self.isRunning == True:
         os.system(self.command)

