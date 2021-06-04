import serial
import sys
import os

monitor_path = '/dev/ttyUSB0'

if not os.path.exists(monitor_path):
    print(F"Device: {monitor_path} not found.")
    sys.exit(1)

