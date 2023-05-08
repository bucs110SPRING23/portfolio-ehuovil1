import random

class Point:

    def __init__(self, x=0, y=0, color="red"):
        self.xcoor = abs(x)
        self.ycoor = abs(y)
        self.color = color
        