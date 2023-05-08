from Rectangle import Rectangle
class Surface:
    def __init__(self, filename, x, y, h, w):
        self.rect = Rectangle(x, y, h, w)
        self.image = filename
    def getRect(self):
        # function description:  the rectangle data from self.rect, which is  the 
        # function for a Rectangle using the x, y, h, and w, parameters
        # args: none
        # returns (self.rect): 
        return self.rect



