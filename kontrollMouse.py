import binascii
import threading
import os

from loopingForKontroll import Looping

def MouseRightStart(ev):
  asciiSysex = binascii.hexlify(ev.sysex)
  global t
  global l
  print ev.sysex
  asciiSysex = binascii.hexlify(ev.sysex)
  print asciiSysex[18:22]
  l = Looping(True, "mouseRight", "/usr/bin/xdotool mousemove_relative --polar 90 1")
  t = threading.Thread(target = l.runForever)
  t.daemon=True
  t.start()

def MouseRightStop(ev):
  l.isRunning = False


def MouseLeftStart(ev):
  asciiSysex = binascii.hexlify(ev.sysex)
  global tleft
  global left
  print ev.sysex
  asciiSysex = binascii.hexlify(ev.sysex)
  print asciiSysex[18:22]
  left = Looping(True, "mouseRight", "/usr/bin/xdotool mousemove_relative --polar 270 1")
  tleft = threading.Thread(target = left.runForever)
  tleft.daemon=True
  tleft.start()

def MouseLeftStop(ev):
  left.isRunning = False



def MouseUpStart(ev):
  asciiSysex = binascii.hexlify(ev.sysex)
  global tup
  global up
  print ev.sysex
  asciiSysex = binascii.hexlify(ev.sysex)
  print asciiSysex[18:22]
  up = Looping(True, "mouseRight", "/usr/bin/xdotool mousemove_relative --polar 0 1")
  tup = threading.Thread(target = up.runForever)
  tup.daemon=True
  tup.start()

def MouseUpStop(ev):
  up.isRunning = False



def MouseDownStart(ev):
  asciiSysex = binascii.hexlify(ev.sysex)
  global tdown
  global down
  print ev.sysex
  asciiSysex = binascii.hexlify(ev.sysex)
  print asciiSysex[18:22]
  down = Looping(True, "mouseRight", "/usr/bin/xdotool mousemove_relative --polar 180 1")
  tdown = threading.Thread(target = down.runForever)
  tdown.daemon=True
  tdown.start()

def MouseDownStop(ev):
  down.isRunning = False


def MouseLeftClick(ev):
  command = '/usr/bin/xdotool click 1'
  os.system(command)

def MouseRightClick(ev):
  command = '/usr/bin/xdotool click 3'
  os.system(command)

