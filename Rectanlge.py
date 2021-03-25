class Rectangle():
    def __init__(self, sigrdze, sigane):
        self.sigrdze = sigrdze
        self.sigane = sigane
    def area(self):
        return self.sigrdze*self.sigane
    def perimeter(self):
        return (self.sigrdze+self.sigane)*2
    def print_info(self):
        return f"Sigrdze = {self.sigrdze}, Sigane = {self.sigane}, Area = {self.area()}, Perimeter = {self.perimeter()}" \

parametrebi = Rectangle(5,6)
print(parametrebi.print_info())



