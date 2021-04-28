import serial

ser = serial.Serial('COM7', 9600)
if not ser.isOpen():
    ser.open()
print('com7 is open\n', ser.isOpen())

recevie = ser.read()
print(recevie)