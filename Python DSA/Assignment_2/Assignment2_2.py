
# 2. Define a class Circle with instance object variable radius. 
# Provide setter and getter for radius. 
# Also define getArea() and getCircumference() methods.

class Circle:
    pi = 3.14
    
    def __init__(self, radius):
        self.radius = radius
        
    def getArea(self):
        area = Circle.pi * self.radius * self.radius
        return area
   
    def getCircumference(self):
        circumference = 2 * Circle.pi * self.radius
        return circumference
    
def main():
    radius = 5  # You need to specify the radius value here
    obj1 = Circle(radius)
    area = obj1.getArea()
    circumference = obj1.getCircumference()
    
    print("Area of the circle:", area)
    print("Circumference of the circle:", circumference)

if __name__ == "__main__":
    main()
    
# The Circle class has a class variable pi instead of x.
# The constructor takes only the radius as a parameter.
# The getArea and getCircumference methods use the 
# pi class variable to perform calculations based on the radius.
# In the main function, you specify the radius value when creating the Circle object,
# and then you calculate and print the area and circumference.