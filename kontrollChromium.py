import binascii
import os

###################################################################
#######  Chrome / Chromium  #######################################
###################################################################

def chromiumActivateWindow(ev):
#  command = '/usr/bin/wmctrl -a Chromium' 
  command = 'xdotool search "Google Chrome" windowactivate --sync key --clearmodifiers ctrl+l'
  os.system(command)

 
def chromiumScrollDown(ev):
#  print ev.sysex                                                                                                                                             
  print(binascii.hexlify(ev.sysex))
  command = 'windowName=$(/usr/bin/xdotool getwindowfocus getwindowname) ; case ${windowName} in  *Chrome* ) /usr/bin/xdotool key Down ;; esac'
  os.system(command)

def chromiumScrollUp(ev):
#  print ev.sysex                                                                                                                                             
  print(binascii.hexlify(ev.sysex))
  command = 'windowName=$(/usr/bin/xdotool getwindowfocus getwindowname) ; case ${windowName} in  *Chromium|Chrome* ) /usr/bin/xdotool key Up ;; esac'
  os.system(command)

def chromiumNextTab(ev):
#  print ev.sysex                                                                                                                                             
  print(binascii.hexlify(ev.sysex))
  command = 'windowName=$(/usr/bin/xdotool getwindowfocus getwindowname) ; case ${windowName} in  *Chromium|Chrome* ) /usr/bin/xdotool key ctrl+Tab ;; esac'
  os.system(command)

def chromiumPrevTab(ev):
#  print ev.sysex                                                                                                                                             
  print(binascii.hexlify(ev.sysex))
  command = 'windowName=$(/usr/bin/xdotool getwindowfocus getwindowname) ; case ${windowName} in  *Chromium|Chrome* ) /usr/bin/xdotool key ctrl+shift+Tab ;; esac'
  os.system(command)
