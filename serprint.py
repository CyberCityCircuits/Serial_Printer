# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:25:32 2017

@author: DREAM
"""


import serial #pySerial
com = 'COM1'
baud = 38400
width = 42
cutfeed = 6

ser = serial.Serial(com, baud, timeout=0,parity=serial.PARITY_NONE)
ser.close()

#Feeds a single line.
def linefeed():
    if not ser.isOpen():
        ser.open()
    ser.write("\n".encode())

#prints a string    
def serprt(item):
    if not ser.isOpen():
        ser.open()
    ser.write(item.encode())
    linefeed()
    #ser.close()

#prints a centered string    
def serprtcent(item):
    if not ser.isOpen():
        ser.open()
    ser.write((item.center(width)).encode())
    ser.write("\n".encode())
    #ser.close()

#cuts the paper    
def cutpaper():
    if not ser.isOpen():
        ser.open()
    line = range(cutfeed)
    for i in line:
        linefeed()
    ser.write(b"\x1D\x56\x00")    
    #ser.close()

#closes the serial connection
#you must end any print process with this command.
def serclose():
    if ser.isOpen():
        ser.close()
        
    
