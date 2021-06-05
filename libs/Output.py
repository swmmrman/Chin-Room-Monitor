import sys
class Output:
    def __init__(self, target):
        self.target = target


    def update_page(self, message):
        f = open(self.target, "w")
        f.write(message)
        f.close()
