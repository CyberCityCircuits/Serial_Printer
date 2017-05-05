
import serial #pySerial
from PIL import Image

com = 'COM1'
baud = 38400
width = 42
cutfeed = 6


ser = serial.Serial(com, baud, timeout=0,parity=serial.PARITY_NONE)

if ser.isOpen():
    ser.close()

ser.close()

#takes a list and will slign it center with so many lines.
#So if you want your list of 5 lines to take up 10 lines this will do it.
def centline(lines, item):
    begin = round((lines-len(item))/2)
    end = lines-begin-len(item)
    beginrge = range(begin)
    endrge = range(end)
    for i in beginrge:
        item.insert(0,"")
    for i in endrge:
        item.append("")
        
#closes the serial connection
#you must end any print process with this command.
def close():
    if ser.isOpen():
        ser.close()

#cuts the paper    
def cutpaper():
    if not ser.isOpen():
        ser.open()
    line = range(cutfeed)
    for i in line:
        linefeed()
    ser.write(b"\x1D\x56\x00")    
    
#shortcut to cutpaper and close the connection
def end():
    cutpaper()
    close()
        
#feeds five lines
def feed05():
    if not ser.isOpen():
        ser.open()    
    ser.write(b"\x1B\x64\x05")    

#resets all commands sent to printer
def init():
    ser.write(b"\x1B\x40")
        
#Feeds a single line.
def linefeed():
    if not ser.isOpen():
        ser.open()
    ser.write(b"\x0a")

#prints a string    
def prt(item):
    if not ser.isOpen():
        ser.open()
    ser.write(item.encode())
    linefeed()
    
#prints a centered string    
def prtcent(item):
    if not ser.isOpen():
        ser.open()
    ser.write((item.center(width)).encode())
    ser.write("\n".encode())
    #ser.close()

#prints a list.        
def prtlst(item):
    for i in item:
        prtcent(i)          
        
#rotates characters clockwise
def rotatecw(item):
    if not ser.isOpen():
        ser.open()    
    if item == 0:#cancels
        ser.write(b"\x1B\x56\x48")
    elif item == 1:#rotates
        ser.write(b"\x1B\x56\x49")

#sets font    
def setfont(item):
    if not ser.isOpen():
        ser.open()        
    if item == 0:#Font A (Full Size)
        ser.write(b"\x1B\x4D\x00")
    elif item == 1:#Font B (Half Size)
        ser.write(b"\x1B\x4D\x01")

#sets justification
def setjust(item):
    if not ser.isOpen():
        ser.open()    
    if item == 0:#left
        ser.write(b"\x1B\x61\x00")
    elif item == 1:#right
        ser.write(b"\x1B\x61\x02")
    elif item == 2:#center
        ser.write(b"\x1B\x61\x01")
    else:
        print("Invalid Entry")        
        
def setsize(item):
    if not ser.isOpen():
        ser.open()        
    if item == 0:#Size Normal
        ser.write(b"\x1D\x21\x00")
    elif item == 1:#Size Double
        ser.write(b"\x1D\x21\x11")    
    elif item == 2:#Size Triple
        ser.write(b"\x1D\x21\x22")          
        
#print text upside down
def upsidedown(item):
    if not ser.isOpen():
        ser.open()        
    if item == 0:#right side up
        ser.write(b"\x1B\x7B\x02")
    elif item == 1:#upside down
        ser.write(b"\x1B\x7B\x01")  
        
###The commands below are for making tables.###

#Makes a Bottom Line Divider
def bottomrow():
    if not ser.isOpen():
        ser.open()
    ser.write(b"\xC0")
    col = range(width-2)
    for i in col:
        ser.write(b"\xC4")
    ser.write(b"\xD9")
    linefeed()

#Makes a Blank Center Row    
def centerrow():
    if not ser.isOpen():
        ser.open()
    ser.write(b"\xB3")
    col = range(width-2)
    for i in col:
        ser.write(b"\xFF")
    ser.write(b"\xB3")    
    linefeed()
    
#same command as center row, but it also has a text field.
def centerrowtext(text):
    if not ser.isOpen():
        ser.open()
    ser.write(b"\xB3")
    col = (width-2)
    ser.write((text.center(col)).encode())
    ser.write(b"\xB3")    
    linefeed()        

#Makes a H-Line to divide text sections.
def dividerrow():
    if not ser.isOpen():
        ser.open()
    ser.write(b"\xC3")
    col = range(width-2)
    for i in col:
        ser.write(b"\xC4")
    ser.write(b"\xB4")   
    linefeed()

#Makes a Top Line Divider
def toprow():
    if not ser.isOpen():
        ser.open()
    ser.write(b"\xDA")
    col = range(width-2)
    for i in col:
        ser.write(b"\xC4")
    ser.write(b"\xBF")
    linefeed()

    
#feeds lines (NOT WORKING)
def feed(item):
    item = str(item).zfill(2)
    if not ser.isOpen():
        ser.open()    
    #ser.write(b("\x1B\x64\x"+item))
    
#prints barcodes (NOT WORKING)
def barcode(item):
    if not ser.isOpen():
        ser.open()        
    

        
def convert_img(item):
    global img
    img = Image.open(item)
    img = img.convert('L')
    img.save("logo_c.bmp")
    
