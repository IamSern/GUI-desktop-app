import serial 

ser = serial.Serial(
    port='COM8',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

# ser = serial.Serial('COM5',9600,)

print("connected to: " + ser.portstr)
#count=1

line = []

while True:
    for c in ser.read():
        line.append(c)
        if c == '\n':
            print("Line: " + ''.join(line))
            line = []
            break

ser.close()