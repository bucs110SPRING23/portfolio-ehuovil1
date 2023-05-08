class Rectangle:
    def __init__(self, x, y, h, w):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
    def __str__(self):
        #returns the properties of self
        #args: none
        #return: string of properties
        return ("x: " + self.x + "y: " + self.y + "width: " + self.width + "height: " + self.height)








