import os
import sys
from collections import OrderedDict

import libs.Stations as Stations
import serial
from libs import Output

outfile = ""
alertfile = ""
try:
    f = open("param.cfg", "r")
    outfile = f.readline().strip("\n")
    alertfile = f.readline().strip("\n")
except FileNotFoundError:
    print("param.cfg is missing.")
    sys.exit(1)

if len(sys.argv) == 2:
    num = sys.argv[1]
else:
    num = 0

monitor_path = f"/dev/tty{num}"

high_temp = 68.5
crit_temp = 75.0

stations = {}

def soundAlarm(station, temp, outfile):
    out = Output.Output(outfile)
    out.update_page(F"Over Station:{station} temp:{temp}f")



if not os.path.exists(monitor_path):
    print(f"Device: {monitor_path} not found.")
    sys.exit(1)
with serial.Serial(monitor_path, 115200) as ser:
    print(ser.readline().decode("utf-8"))  # discard startup line
    pageFile = Output.Output(outfile)
    alertFile = Output.Output(alertfile)
    while True:
        out = ""
        pre = f"\033[{len(stations) * 3}A"
        line = ser.readline().decode("utf-8").strip()
        (station, temp, humidity, count) = line.split()
        station_number = station.strip("R")
        uptime = count.split(":")[1]
        temp = float(temp.strip("f"))
        humidity = float(humidity.strip("%"))
        if station_number not in stations:
            stations[station_number] = Stations.Station(station_number, temp, humidity)
            stations = OrderedDict(sorted(stations.items()))
        else:
            stations[station_number].update(temp, humidity)
        for st in stations.values():
            out += st.print_station()
        print(f"{pre}{out}", end="")
        cleanout = out.replace("\033[K", "")
        pageFile.update_page(cleanout)
        #if temp > crit_temp:
        #    soundAlarm(station_number, temp, outfile)
        #elif temp > high_temp:
            #soundAlarm(station_number, temp, outfile)
