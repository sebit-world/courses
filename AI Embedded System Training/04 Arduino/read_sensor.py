import serial

serial_port = serial.Serial("/dev/ttyUSB0", 9600)
while 1:
    try:
        data = serial_port.readline().decode("utf-8").strip()
        print(data)
    except KeyboardInterrupt:
        break
serial_port.close()
