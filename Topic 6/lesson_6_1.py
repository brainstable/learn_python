class Parallelepiped:

    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height

    def calculate_volume(self):
        return self.calculate_area_base() * self.height

    def calculate_area_base(self):
        return self.width * self.length

    def calculate_area_side(self):
        return 2 * (self.width + self.length) * self.height

paral = Parallelepiped(4, 5, 6)
print(paral.calculate_volume())
print(paral.calculate_area_base())
print(paral.calculate_area_side())