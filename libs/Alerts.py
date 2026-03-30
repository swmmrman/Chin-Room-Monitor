class Alert:
    def __init__(self, number, temp):
        self.number = number
        self.temp = temp

    def update(self, temp):
        self.temp = temp

    def print_alert(self):
        crit_temp = 75
        high_temp = 72
        if self.temp > crit_temp:
            return f"Crit Temp Station {self.number}: {self.temp}"
        elif self.temp > high_temp:
            return f"High Temp Station {self.number}: {self.temp}"
        else:
            return ""
