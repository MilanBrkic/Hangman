class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printSelf(self):
        print(self.x, self.y)

class Line:
    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

class WidthLimits:
    def __init__(self, width, pomeraj):
        self.lower = width
        self.upper = width + pomeraj

class HeightLimits:
    def __init__(self, height, pomeraj):
        self.lower = height
        self.upper = height + pomeraj

class DimensionLimits:
    def __init__(self,syllable,width, height):
        self.syllable = syllable
        self.width = width
        self.height = height