import math


class Station:
    def __init__(self, number, temp, humidity):
        self.number = number
        self.high_temp = temp
        self.low_temp = temp
        self.current_temp = temp
        self.high_humidity = humidity
        self.low_humidity = humidity
        self.current_humidity = humidity

    def update(self, temp, humidity):
        self.current_humidity = humidity
        self.current_temp = temp
        if self.high_temp < temp or math.isnan(self.high_temp):
            self.high_temp = temp
        elif self.low_temp > temp or math.isnan(self.low_temp):
            self.low_temp = temp
        if self.high_humidity < humidity or math.isnan(self.high_humidity):
            self.high_humidity = humidity
        elif self.low_humidity > humidity or math.isnan(self.low_humidity):
            self.low_humidity = humidity

    def print_station(self):
        ###Print a station out"""
        return (
            f"\033[KStation: {self.number} \t\t\t\t\t {self.number}\n"
            f"\033[KTemperature: \tMin:{self.low_temp: 3.1f}f Max:{self.high_temp: 3.1f}f\tCur:{self.current_temp: 3.1f}f\n"
            f"\033[KHumidity: \tMin:{self.low_humidity: 3.1f}% Max:{self.high_humidity: 3.1f}%\tCur:{self.current_humidity: 3.1f}%\n"
        )
