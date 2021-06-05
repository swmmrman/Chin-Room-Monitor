import serial
import sys
import os
import libs.Stations as Stations
from libs import Output

outfile = ""
try:
    f = open("param.cfg", "r")
    outfile = f.readline().strip("\n")
except FileNotFoundError:
    print("param.cfg is missing.")
    sys.exit(1)

monitor_path = '/dev/ttyUSB0'
high_temp = 68.5
crit_temp = 72.5

stations = {}

def soundAlarm(station, temp, outfile):
    alert_type = "High"
    # dummy function
    for key, value in kwargs:
        if key == crit and value:
            alert_type="Critical"
    out = Output.Output(outfile)
    out.update_page(F"Over Station:{station} temp:{temp}f")
            # other crit code here.
    #print(F"{alert_type} temp reached on Station {station}: {temp}f")



if not os.path.exists(monitor_path):
    print(F"Device: {monitor_path} not found.")
    sys.exit(1)
with serial.Serial(monitor_path, 115200) as ser:
    print(ser.readline().decode('utf-8')) #discard startup line
    while True:
        print(F"\033[{len(stations)*3}A", end="")
        line = ser.readline().decode('utf-8').strip()
        (station, temp, humidity, count) = line.split()
        station_number = station.strip("R")
        uptime = count.split(":")[1]
        temp = float(temp.strip('f'))
        humidity = float(humidity.strip("%"))
        if station_number not in stations:
            stations[station_number] = Stations.Station(station_number, temp, humidity)
        else:
            stations[station_number].update(temp, humidity)
        for st in stations.values():
            st.print_station()
        if temp > crit_temp:
            soundAlarm(station_number, temp, outfile)
        #elif temp > high_temp:
            #soundAlarm(station_number, temp, outfile)
