from Poly.Point import Point
from Poly.Polygon import Polygon

square = Polygon()
square.add_point(Point(1, 1))
square.add_point(Point(1, 2))
square.add_point(Point(2, 2))
square.add_point(Point(2, 1))

print(square.perimeter())
