from Rectangle.py import Rectangle
class Surface:
    def __init__(self, filename, x, y, h, w):
        self.rect = x, y, h, w
        self.image = filename