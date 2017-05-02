import math


class Point:
    def __init__(self, x, y):
        """
        Initializes a point in 2D coordinates as x and y
        :param x: 
        :param y:
        """
        self.x = x
        self.y = y

    def distance(self, p2):
        """
        Find's Distance b2n two 2D points
        :param p2: 
        :return: Distance b2n
        """
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)
