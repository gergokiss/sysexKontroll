import binascii
import os
import threading

from loopingForKontroll import Looping


###################################################################
#######  Avidemux  ################################################
################################################################### 

def activateAvidemuxWindow(ev):
  command = 'dotool search "Avidemux" windowactivate --sync key --clearmodifiers ctrl+l'
  os.system(command)


def avidemuxFrameStepSysex(ev):                                                                                                         
#  print ev.sysex                                                                                                                                             
  print(binascii.hexlify(ev.sysex))                                                                                                                            
  command = 'windowName=$(/usr/bin/xdotool getwindowfocus getwindowname) ; case ${windowName} in  *Avidemux* ) /usr/bin/xdotool key Right ;; esac'
  os.system(command)

def avidemuxFrameBackStepSysex(ev):                                                                                                         
  print ev.sysex                                                                                                                                             
  print(binascii.hexlify(ev.sysex))                                                                                                                            
  command = 'windowName=$(/usr/bin/xdotool getwindowfocus getwindowname) ; case ${windowName} in  *Avidemux* ) /usr/bin/xdotool key Left ;; esac'
  os.system(command)

def avidemuxPlay(ev):                                                                                                         
  print ev.sysex                                                                                                                                             
  print(binascii.hexlify(ev.sysex))                                                                                                                            
  command = 'windowName=$(/usr/bin/xdotool getwindowfocus getwindowname) ; case ${windowName} in  *Avidemux* ) /usr/bin/xdotool key space ;; esac'
  os.system(command)

def avidemuxForwardStart(ev):
  asciiSysex = binascii.hexlify(ev.sysex)                                                                                                                      
  global tforward
  global forward
  print ev.sysex                                                                                                                                            
  asciiSysex = binascii.hexlify(ev.sysex)                                                                                                                      
  print asciiSysex[18:22]                                                                                                                                      
  forward = Looping(True, "avidemuxForward", "windowName=$(/usr/bin/xdotool getwindowfocus getwindowname) ; case ${windowName} in  *Avidemux* ) /usr/bin/xdotool key Up ;;  esac")
  tforward = threading.Thread(target = forward.runForever)
  tforward.daemon=True
  tforward.start() 

def avidemuxForwardStop(ev):                                                                                                         
  forward.isRunning = False 

def avidemuxBackwardStart(ev):
  asciiSysex = binascii.hexlify(ev.sysex)                                                                                                                      
  global tbackward
  global backward
  print ev.sysex                                                                                                                                            
  asciiSysex = binascii.hexlify(ev.sysex)                                                                                                                      
  print asciiSysex[18:22]                                                                                                                                      
  backward = Looping(True, "avidemuxBackward", "windowName=$(/usr/bin/xdotool getwindowfocus getwindowname) ; case ${windowName} in  *Avidemux* ) /usr/bin/xdotool key Down ;;  esac")
  tbackward = threading.Thread(target = backward.runForever)
  tbackward.daemon=True
  tbackward.start() 

def avidemuxBackwardStop(ev):                                                                                                         
  backward.isRunning = False 

def avidemuxNextIntraFrame(ev):                                                                                                         
  command = 'windowName=$(/usr/bin/xdotool getwindowfocus getwindowname) ; case ${windowName} in  *Avidemux* ) /usr/bin/xdotool key Up ;;  esac' 
  os.system(command)

def avidemuxPrevIntraFrame(ev):                                                                                                         
  command = 'windowName=$(/usr/bin/xdotool getwindowfocus getwindowname) ; case ${windowName} in  *Avidemux* ) /usr/bin/xdotool key Down ;;  esac' 
  os.system(command)

def avidemuxSetMarkStart(ev):                                                                                                         
  command = '/usr/bin/xdotool key bracketleft' 
  os.system(command)

def avidemuxSetMarkEnd(ev):                                                                                                         
  command = '/usr/bin/xdotool key bracketright' 
  os.system(command)

def avidemuxCutMarked(ev):                                                                                                         
  command = '/usr/bin/xdotool key ctrl+x' 
  os.system(command)
