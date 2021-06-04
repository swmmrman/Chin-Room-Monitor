import serial
import sys
import os

monitor_path = '/dev/ttyUSB0'

if not os.path.exists(monitor_path):
    print(F"Device: {monitor_path} not found.")
    sys.exit(1)

with serial.Serial(monitor_path, 115200) as ser:
    ser.readline() #discard startup line
    while True:
        line = ser.readline().decode('utf-8').strip()
        (station, temp, humidity, count) = line.split()
        station_number = station.strip("R")
        uptime = count.split(":")[1]
        print(F"Station: {station_number} Status: {temp}, {humidity} Uptime:{uptime}")
