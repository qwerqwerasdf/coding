from mymath import PI   # mymath.py에서 PI 불러오기

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2
    
    def circumference(self):
        return 2 * PI * self.radius
