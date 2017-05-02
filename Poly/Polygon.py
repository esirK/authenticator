class Polygon:
    def __init__(self):
        self.vertices = []

    def add_point(self, point):
        self.vertices.append(point)

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter
