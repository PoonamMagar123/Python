class Demo:
    def __init__(self,A,B):
        print("Inside constructor")
        self.No1 = A
        self.No2 = B

    def Fun(self):
        print("Value 1 :",self.No1)
        print("Value 2 :",self.No2)

    def Gun(self):
        print("Value 3 :",self.No1)
        print("Value 4 :",self.No2)

def main():
  
    obj1 = Demo(11,22)
  
    obj2 = Demo(51,101)
    
    print("Calling instance methods for Obj1:")
    obj1.Fun()
    obj1.Gun()
    
    print("Calling instance methods for Obj2:")
    obj2.Fun()
    obj2.Gun()
    
    
if __name__ == "__main__":
    main()