class station:
    def __init__(self, number, temp, humidity):
        self.number = number
        self.high_temp = temp
        self.low_temp = temp
        self.high_humidity = humidity
        self.low_humidity = humidity

    def update(self, temp, humidity):
        if self.high_temp < temp:
            self.high_temp = temp
        elif self.low_temp > temp:
            self.low_temp = temp
        if self.high_humidity < humidity:
            self.high_humidity = humidity
        elif self.low_humidity > humidity:
            self.low_humidity = humidity
