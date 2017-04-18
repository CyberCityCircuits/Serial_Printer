# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 08:44:56 2017

@author: DREAM
"""

import serprint

width = 42

serprint.ser.open()


def toprow():
    if not serprint.ser.isOpen():
        serprint.ser.open()
    serprint.ser.write(b"\xDA")
    col = range(width-2)
    for i in col:
        serprint.ser.write(b"\xC4")
    serprint.ser.write(b"\xBF")
    
def bottomrow():
    if not serprint.ser.isOpen():
        serprint.ser.open()
    serprint.ser.write(b"\xC0")
    col = range(width-2)
    for i in col:
        serprint.ser.write(b"\xC4")
    serprint.ser.write(b"\xD9")
    
def centerrow():
    if not serprint.ser.isOpen():
        serprint.ser.open()
    serprint.ser.write(b"\xB3")
    col = range(width-2)
    for i in col:
        serprint.ser.write(b"\xFF")
    serprint.ser.write(b"\xB3")    
    
def dividerrow():
    if not serprint.ser.isOpen():
        serprint.ser.open()
    serprint.ser.write(b"\xC3")
    col = range(width-2)
    for i in col:
        serprint.ser.write(b"\xC4")
    serprint.ser.write(b"\xB4")   
    
def centerrowtext(text):
    if not serprint.ser.isOpen():
        serprint.ser.open()
    serprint.ser.write(b"\xB3")
    col = (width-2)
    serprint.ser.write((text.center(col)).encode())
    serprint.ser.write(b"\xB3")    
    
def end():    
    serprint.cutpaper()
    serprint.serclose()
    
toprow()
#serprint.serclose()
centerrow()
#serprint.serclose()
centerrowtext("This is TEST")
#serprint.serclose()
centerrow()
dividerrow()
centerrow()
centerrowtext("Pretty Neat!")
centerrow()
#serprint.serclose()
bottomrow()
end()
