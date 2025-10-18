class Shape:
    def no_of_sides(self):
        print("This shape has many sides")

class Square(Shape):
    def no_of_sides(self):
        print("A square has 4 sides")

#Creating objects
s1 = Shape()
s2 = Square()
#Calling the method
s1.no_of_sides() #Parent class method
s2.no_of_sides() #Child class overrides the method
