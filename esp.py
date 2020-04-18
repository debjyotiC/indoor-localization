import serial


def esp_serial():
    serial_data = []
    ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 115200)
    for i in range(4):
        serial_data.append(int(ser.read(3)))
    return serial_data
