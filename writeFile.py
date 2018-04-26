import serial
import numpy as np
from PIL import Image

#setup serial
ser = serial.Serial('/dev/ttyAMA0', 115200, timeout = 1)
print('Serial Connected')


f = open('test.png', 'wb')
data = False
timeout = 0
reads = 0
try:
    while not timeout > 2:
        read = ser.read(100000)
        if str(read) != "b''":    
            data = True
            timeout = 0
            f.write(read)
            reads += 1
        if data == True and str(read) == "b''":
            timeout += 1
    f.close()
    print('File written.')
    print('Non-empty reads: ', reads)
except KeyboardInterrupt:
    f.close()
    print('Terminated.')
    pass
