import serial
import sys
import os

monitor_path = '/dev/ttyUSB0'
high_temp = 66
crit_temp = 67

def soundAlarm(station, temp, **kwargs):
    alert_type = "High"
    # dummy function
    for key, value in kwargs:
        if key == crit and value:
            alert_type="Critical"
            # other crit code here.
    print(F"{alert_type} temp reached on Station {station}: {temp}f")



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
        temp = float(temp.strip('f'))
        if temp > high_temp:
            soundAlarm(station_number, temp)
        elif temp > crit_temp:
            soundAlarm(station_number, temp, crit=True)
        print(F"Station: {station_number} Status: {temp}f, {humidity} Uptime:{uptime}")
