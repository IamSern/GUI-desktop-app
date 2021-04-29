import serial

ser = serial.Serial(port='COM9', baudrate= 9600, bytesize= 8, 
                        timeout= 2, stopbits= serial.STOPBITS_ONE)
if not ser.isOpen():
    ser.open()
print('COM9 is open:', ser.isOpen())
#print(serial.tools.list_ports)
recevie = ser.read(4)
print(recevie)
