
# 1. Define a python class Person with instance object variables name and age. 
# Set Instance object variables in __init__() method. 
# Also define show() method to display name and age of a person.
class Person:
    def __init__(self, Name, Age):
        self.name  = Name
        self.age = Age
        
    def Show(self):
        print("Name : {} , Age : {}".format(self.name,self.age))
        
def main():
    
    obj1 = Person('Tushar',23)
    obj1.Show()
    
if __name__ == "__main__":
    main()
    
    # Your code defines a Person class with an __init__ method to initialize the name 
    # and age attributes, as well as a Show method to display the person's name and age. 
    # In the main() function, an instance of the Person class is created,
    # and the Show method is called to display the person's information.
        