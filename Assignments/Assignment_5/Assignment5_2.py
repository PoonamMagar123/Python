class Circle:
    PI = 3.14
    
    def __init__(self,radius):
        print("Inside constructor")
        self.Radius = radius
        
    def CalculateArea(self):
        Area = 0
        Area = Circle.PI * self.Radius * self.Radius
        return Area

    def CalculateCircumference(self):
        Circumference = 0
        Circumference = 2 * Circle.PI * self.Radius
        return Circumference

def main():
    r = int(input("Enter The radius : "))
    obj1 = Circle(r)
    
    Area = obj1.CalculateArea()
    print("Area of circle is : ",Area)
    
    Circumference = obj1.CalculateCircumference()
    print("Circumference of circle  is : ",Circumference)
    
    
    r = int(input("Enter The radius : "))
    obj2 = Circle(r)
    
    Area = obj2.CalculateArea()
    print("Area of circle is : ",Area)
    
    Circumference = obj2.CalculateCircumference()
    print("Circumference of circle  is : ",Circumference)

     
    r = int(input("Enter The radius : "))
    obj3 = Circle(r)
    
    Area = obj3.CalculateArea()
    print("Area of circle is : ",Area)
    
    Circumference = obj3.CalculateCircumference()
    print("Circumference of circle  is : ",Circumference)
    
    
if __name__ == "__main__":
    main()