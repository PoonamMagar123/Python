
# 3. Define a class Rectangle with length and breadth as instance object variables. 
# Provide setDimensions(), showDimensions() and getArea() method in it

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def setDimensions(self, length, breadth):
        self.length = length
        self.length = length
        self.breadth = breadth
    
    def showDimensions(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)
    
    def getArea(self):
        return self.length * self.breadth

# Example usage of the Rectangle class
def main():
    # Creating a Rectangle object with initial dimensions
    rectangle1 = Rectangle(5, 10)
    
    # Showing initial dimensions
    print("Initial Dimensions:")
    rectangle1.showDimensions()
    
    # Modifying dimensions using setDimensions() method
    rectangle1.setDimensions(7, 14)
    
    # Showing modified dimensions
    print("\nModified Dimensions:")
    rectangle1.showDimensions()
    
    # Calculating and displaying area
    area = rectangle1.getArea()
    print("\nArea of the rectangle:", area)

if __name__ == "__main__":
    main()
    
# The Rectangle class has instance variables length and breadth initialized through the constructor.
# The setDimensions() method allows you to change the dimensions of the rectangle.
# The showDimensions() method displays the length and breadth of the rectangle.
# The getArea() method calculates and returns the area of the rectangle.
# In the main() function, an instance of the Rectangle class is created, its dimensions are displayed,
# then modified, and the updated dimensions and area are displayed.