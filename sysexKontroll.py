import sys 
import getopt
import binascii  
import commands
import os
import threading

from threading import Thread
from mididings import *
from mididings import event                                                                                                                                    
from kontrollMouse import *
from kontrollChromium import *
from kontrollAvidemux import * 


print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)


def convert_hexstring(s): 
  result = [] 
  for group in s.split(): 
      for hex in (group[i:i+2] for i in range(0, len(group), 2)): 
          result.append(int(hex, 16)) 
  return result 







def printSysex(ev):                                                                                                                                            
#  print ev.sysex                                                                                                                                              
  asciiSysex = binascii.hexlify(ev.sysex)                                                                                                                      
  print(binascii.hexlify(ev.sysex))                                                                                                                            
  print '%.5s' % (binascii.hexlify(ev.sysex))                                                                                                                  
  print asciiSysex[16:18]                                                                                                                                      
  print asciiSysex[18:20]                                                                                                                                      
  midiCC = int(asciiSysex[18:20],16)                                                                                                                           
  print midiCC                                                                                                                                                 
  print event.CtrlEvent(1,1,9,midiCC )                                                                                                                         
  print Ctrl(1,1,9,midiCC)                                                                                                                                     
  return event.CtrlEvent(1,1,9,midiCC )                                                                                                                        



def midi(midiClientName, midiOutputPort, midiInputPort, midiInitScene):

  config(
         client_name = midiClientName,                                                                                                                  
         out_ports = [midiOutputPort],                                                                                                                  
         in_ports = [midiInputPort],                                                                                                                 
         initial_scene = midiInitScene,
	 start_delay = 0.5,
  )


  run(                                                                   
    scenes = {                                                         
        1:  Scene("Avidemux",                                    
               [                                                                                                                                              
               

			ChannelFilter(1) >> CtrlMap(7,14) >> Port(1),
			ChannelFilter(2) >> CtrlMap(7,15) >> Channel(1) >> Port(1),
			ChannelFilter(3) >> CtrlMap(7,16) >> Channel(1) >> Port(1),
			ChannelFilter(4) >> CtrlMap(7,17) >> Channel(1) >> Port(1),
			ChannelFilter(5) >> CtrlMap(7,18) >> Channel(1) >> Port(1),
			ChannelFilter(6) >> CtrlMap(7,19) >> Channel(1) >> Port(1),
			ChannelFilter(7) >> CtrlMap(7,20) >> Channel(1) >> Port(1),
			ChannelFilter(8) >> CtrlMap(7,21) >> Channel(1) >> Port(1),
			ChannelFilter(9) >> CtrlMap(7,22) >> Channel(1) >> Port(1),
			ChannelFilter(10) >> CtrlMap(7,23) >> Channel(1) >> Port(1),
			ChannelFilter(11) >> CtrlMap(7,24) >> Channel(1) >> Port(1),
			ChannelFilter(12) >> CtrlMap(7,25) >> Channel(1) >> Port(1),
			ChannelFilter(13) >> CtrlMap(7,26) >> Channel(1) >> Port(1),
			ChannelFilter(14) >> CtrlMap(7,27) >> Channel(1) >> Port(1),
			ChannelFilter(15) >> CtrlMap(7,28) >> Channel(1) >> Port(1),
			ChannelFilter(16) >> CtrlMap(7,29) >> Channel(1) >> Port(1),


#        [SysExFilter('\xf0\x41\x10\x00\x21\x12\x30\x10\x00') >> Process(mplayerBrightness),] >> Output(1,1),

##########################
## Window without Shift ##
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 07 01 48 f7')) >> Call(activateAvidemuxWindow),],
#        [SysExFilter('\xf0\x41\x10\x00\x21\x12\x30\x00\x11\x00\x3f\xf7') >> Call(avidemuxMouseDownStop),],


##############################
#### Avidemux Play  ##########
##############################                                                                                                                                 
### Roland U8 --> Play #######                                                                                                                                 
##############################                                                                                                                                 
#        SysExFilter('\xf0\x41\x10\x00\x21\x12\x30\x00\x1b\x01\x34\xf7') >> NoteOn(1,1,42,100) >> Port(1), 
#        SysExFilter('\xf0\x41\x10\x00\x21\x12\x30\x00\x1b\x00\x35\xf7') >> NoteOff(1,1,42,0) >> Port(1),
        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 1b 01 34 f7')) >> Call(avidemuxPlay) >> Port(1), 
######################################                                                         
### Roland U8 --> Shift + Play ####### 
######################################  
        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 1b 11 24 f7')) >> Call(avidemuxPlay) >> Port(1), 
##############################
#### Avidemux Stop  ##########
##############################
### Roland U8 --> Stop ####### 
############################## 
#        SysExFilter('\xf0\x41\x10\x00\x21\x12\x30\x00\x1a\x41\x75\xf7') >> NoteOn(1,1,52,100) >> Port(1), 
#        SysExFilter('\xf0\x41\x10\x00\x21\x12\x30\x00\x1a\x40\x76\xf7') >> NoteOff(1,1,52,0) >> Port(1),
        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 1a 41 75 f7')) >> Call(avidemuxPlay), 
######################################                                                         
### Roland U8 --> Shift + Stop ####### 
######################################  
        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 1a 51 65 f7')) >> Call(avidemuxPlay), 
################################################# 
### Roland U8 --> Play while Stop is down ####### 
################################################# 
        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 1b 41 74 f7')) >> NoteOn(1,1,42,100) >> Port(1), 
        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 1b 40 75 f7')) >> NoteOff(1,1,42,0) >> Port(1),


################################################# 
### Frame Forward/Backward ####### 
################################################# 
################
## Time/Value ##
## Forward ##
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 01')) >> Call(avidemuxFrameStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 02')) >> Call(avidemuxFrameStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 03')) >> Call(avidemuxFrameStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 04')) >> Call(avidemuxFrameStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 05')) >> Call(avidemuxFrameStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 06')) >> Call(avidemuxFrameStepSysex),] >> Output(1,1),
## Shift + Forward ##
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 11')) >> Call(avidemuxFrameStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 12')) >> Call(avidemuxFrameStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 13')) >> Call(avidemuxFrameStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 14')) >> Call(avidemuxFrameStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 15')) >> Call(avidemuxFrameStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 16')) >> Call(avidemuxFrameStepSysex),] >> Output(1,1),
## Backward ##
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 0f')) >> Call(avidemuxFrameBackStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 0e')) >> Call(avidemuxFrameBackStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 0d')) >> Call(avidemuxFrameBackStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 0c')) >> Call(avidemuxFrameBackStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 0b')) >> Call(avidemuxFrameBackStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 0a')) >> Call(avidemuxFrameBackStepSysex),] >> Output(1,1),
## Shift + Backward ##
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 1f')) >> Call(avidemuxFrameBackStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 1e')) >> Call(avidemuxFrameBackStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 1d')) >> Call(avidemuxFrameBackStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 1c')) >> Call(avidemuxFrameBackStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 1b')) >> Call(avidemuxFrameBackStepSysex),] >> Output(1,1),
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 1a')) >> Call(avidemuxFrameBackStepSysex),] >> Output(1,1),



################################################# 
### Roland U8 --> Forward ####### 
################################################# 
########
## >> ##
        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 19 01 36 f7')) >> Call(avidemuxForwardStart), 
        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 19 00 37 f7')) >> Call(avidemuxForwardStop), 
################################################# 
### Roland U8 --> Backward ####### 
#################################################
########
## << ## 
        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 18 01 37 f7')) >> Call(avidemuxBackwardStart), 
        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 18 00 38 f7')) >> Call(avidemuxBackwardStop), 

################################################# 
### Roland U8 --> Next Intra Frame ############## 
#################################################
############
## Master ##
#        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 10 78')) >> Call(avidemuxNextIntraFrame),
##################
## Shift + Stop ##
#        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 1a 51 65 f7')) >> Call(avidemuxNextIntraFrame), 
################
## Shift + >> ##
        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 19 11 26 f7')) >> Call(avidemuxNextIntraFrame), 
#        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 19 10 27 f7')) >> Call(avidemuxForwardStop), 
################################################# 
### Roland U8 --> Prev Intra Frame ############## 
#################################################
######### 
## |<< ##
#        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 17 01 38 f7')) >> Call(avidemuxPrevIntraFrame), 
#################
## Shift + |<< ##
#        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 17 11 28 f7')) >> Call(avidemuxPrevIntraFrame), 
################
## Shift + << ## 
        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 18 11 27 f7')) >> Call(avidemuxPrevIntraFrame), 
#        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 18 10 28 f7')) >> Call(avidemuxBackwardStop), 


################################################# 
### Roland U8 --> Set marker 1 (shift+Prev) #####
################################################# 
        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 0e 11 31 f7')) >> Call(avidemuxSetMarkStart), 
################################################# 
### Roland U8 --> Set marker 2 (shift+Next) #####
################################################# 
        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 0f 11 30 f7')) >> Call(avidemuxSetMarkEnd), 
################################################# 
### Roland U8 --> Cut marked (shift+Rec) #####
################################################# 
        SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 1c 11 23 f7')) >> Call(avidemuxCutMarked), 
 
		]
            ),                                                         
        2:  Scene("channel 2, program 23",                             
                Channel(2),                                            
                Program(23) >> Channel(2)                              
            ),                                                         
        3:  Scene("Chromium",                             
		[
##########################
## Window without Shift ##
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 07 01 48 f7')) >> Call(chromiumActivateWindow),],
################################################# 
### Scroll Up / Down  ########################### 
################################################# 
################
## Time/Value ##
## Forward ##
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 01')) >> Call(chromiumScrollDown),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 02')) >> Call(chromiumScrollDown),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 03')) >> Call(chromiumScrollDown),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 04')) >> Call(chromiumScrollDown),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 05')) >> Call(chromiumScrollDown),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 06')) >> Call(chromiumScrollDown),],
## Shift + Forward ##
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 11')) >> Call(chromiumScrollDown),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 12')) >> Call(chromiumScrollDown),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 13')) >> Call(chromiumScrollDown),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 14')) >> Call(chromiumScrollDown),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 15')) >> Call(chromiumScrollDown),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 16')) >> Call(chromiumScrollDown),],
## Backward ##
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 0f')) >> Call(chromiumScrollUp),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 0e')) >> Call(chromiumScrollUp),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 0d')) >> Call(chromiumScrollUp),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 0c')) >> Call(chromiumScrollUp),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 0b')) >> Call(chromiumScrollUp),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 0a')) >> Call(chromiumScrollUp),],
## Shift + Backward ##
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 1f')) >> Call(chromiumScrollUp),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 1e')) >> Call(chromiumScrollUp),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 1d')) >> Call(chromiumScrollUp),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 1c')) >> Call(chromiumScrollUp),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 1b')) >> Call(chromiumScrollUp),],
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 30 00 1a')) >> Call(chromiumScrollUp),],

################################################# 
### Next Tab  ################################### 
################################################# 
### Roland U-8: ##########################
###             AUTO PUNCH  ##############
########################################## 
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 0c 01 43 f7')) >> Call(chromiumNextTab),],
################################################# 
### Previous Tab  ############################### 
################################################# 
### Roland U-8: ##########################
###             LOOP  ####################
########################################## 
        [SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 0b 01 44 f7')) >> Call(chromiumPrevTab),],

		]
            ),                                                         
        4:  Scene("channel 1/3 split",                                 
                KeySplit('c3',                                         
                    Channel(1),                                        
                    Channel(3)                                         
                )                                                      
            ),                                                         
    },                                                                 
    control = ([
##########################################
## Switch Scenes with MIDI      ##########
##########################################

		ChannelFilter(16) >> Filter(PROGRAM) >> SceneSwitch(),                       
 
##########################################
## Switch Scene to 1 (Avidemux) ##########
##########################################
### Roland U-8: ##########################
### Shift+Track Status 1 on MIDI 9-16  ###
########################################## 
		SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 02 30 11 0d f7')) >> Program(1,16,1) >> SceneSwitch(),

##########################################
## Switch Scene to 3 (Chromium) ##########
##########################################
### Roland U-8: ##########################
### Shift+Track Status 3 on MIDI 9-16  ###
########################################## 
		SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 02 32 11 0b f7')) >> Program(1,16,3) >> SceneSwitch(),

##########################################
#### Scene independent processing ########
    		SysExFilter(convert_hexstring('f0 41 10')) >> Print('sysex'),                                   

##Cursor to Mouse###
#        [SysExFilter('\xf0\x41\x10\x00\x21\x12\x30\x00\x16\x01\x39\xf7') >> Call(thread=avidemuxMouseRight),] >> Output(1,1),
#Right#
		SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 16 01 39 f7')) >> Call(MouseRightStart),
		SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 16 00 3a f7')) >> Call(MouseRightStop),
#Left#
		SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 15 01 3a f7')) >> Call(MouseLeftStart),
		SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 15 00 3b f7')) >> Call(MouseLeftStop),
#Up#
		SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 13 01 3c f7')) >> Call(MouseUpStart),
		SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 13 00 3d f7')) >> Call(MouseUpStop),
#Down#
		SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 14 01 3b f7')) >> Call(MouseDownStart),
		SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 14 00 3c f7')) >> Call(MouseDownStop),

#########################
#  Mouse left click  ####
##########################################
### Roland U-8: ##########################
###             ENTER / YES  #############
########################################## 
		SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 11 01 3e f7')) >> Call(MouseLeftClick),
#########################
#  Mouse right click  ####
##########################################
### Roland U-8: ##########################
###             EXIT / NO  #############
########################################## 
		SysExFilter(convert_hexstring('f0 41 10 00 21 12 30 00 12 01 3d f7')) >> Call(MouseRightClick),
               ]
              ),
    pre = ~Filter(PROGRAM),                                           
  )    


def main(argv):
   clientName = ''
   outputport = ''
   inputport = ''
   initScene = ''
   try:
      opts, args = getopt.getopt(argv,"hc:o:i:s:",["cName=","oport=","iport=","scene=",])
   except getopt.GetoptError:
      print 'totalKontrol.py -c <clientName> -o <outputPort> -i <inputPort> -s <initScene>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'totalKontrol.py -c <clientName> -o <outputPort> -i <inputPort> -s <initScene>'
         sys.exit()
      elif opt in ("-c", "--cName"):
         clientName = arg
      elif opt in ("-o", "--oport"):
         outputPort = arg
      elif opt in ("-i", "--iport"):
         inputPort = arg
      elif opt in ("-s", "--scene"):
         initScene = int(arg)
   print 'Client name is "', clientName
   print 'Output port is "', outputPort
   print 'Input port is "', inputPort
   print 'Init scene is "', initScene

   midi(clientName, outputPort, inputPort, initScene)

if __name__ == "__main__":
   main(sys.argv[1:])


