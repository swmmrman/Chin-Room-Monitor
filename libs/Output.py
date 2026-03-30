import os
import sys


class Output:
    def __init__(self, target):
        self.target = target
        parts = target.split("/")
        dir = "/".join(parts[0:-1])
        if not os.path.exists(dir):
            os.makedirs(dir)
        f = open(target, "w")
        f.write("")
        f.close()

    def update_page(self, message):
        f = open(self.target, "w")
        f.write(message)
        f.close()
