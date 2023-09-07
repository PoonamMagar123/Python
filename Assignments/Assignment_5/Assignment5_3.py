class Arithmatic:
    def __init__(self,A,B):
        print("Inside constructor")
        self.No1 = A
        self.No2 = B
        
    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans
    
    def Multiplication(self):
        Ans = 0
        Ans = self.No1 * self.No2
        return Ans
    
    def Division(self):
        Ans = 0
        Ans = self.No1 / self.No2
        return Ans
    
def main():
    #obj1
    
    Value1 = int(input("Enter First number :" ))
    Value2 = int(input("Enter Second number :" ))
    
    obj1 = Arithmatic(Value1, Value2)
    
    Ret = obj1.Addition()
    print("Addition is :", Ret)
    
    Ret = obj1.Substraction()
    print("Substraction is :", Ret)
    
    Ret = obj1.Multiplication()
    print("Multiplication is :", Ret)
    
    Ret = obj1.Division()
    print("Division is :", Ret)
     
    #obj2
    
    Value1 = int(input("Enter First number : " ))
    Value2 = int(input("Enter Second number : " ))
   
    obj2 = Arithmatic(Value1, Value2)
    
    Ret = obj2.Addition()
    print("Addition is :", Ret)
    
    Ret = obj2.Substraction()
    print("Substraction is :", Ret)
    
    Ret = obj2.Multiplication()
    print("Multiplication is :", Ret)
    
    Ret = obj2.Division()
    print("Division is :", Ret)
    
    #obj3
     
    Value1 = int(input("Enter First number :" ))
    Value2 = int(input("Enter Second number :" ))
    
    obj3 = Arithmatic(Value1, Value2)
    
    Ret = obj3.Addition()
    print("Addition is :", Ret)
    
    Ret = obj3.Substraction()
    print("Substraction is :", Ret)
    
    Ret = obj3.Multiplication()
    print("Multiplication is :", Ret)
    
    Ret = obj3.Division()
    print("Division is :", Ret)
    
    #obj4
     
    Value1 = int(input("Enter First number :" ))
    Value2 = int(input("Enter Second number :" ))
    
    obj4 = Arithmatic(Value1, Value2)
    
    Ret = obj4.Addition()
    print("Addition is :", Ret)
    
    Ret = obj4.Substraction()
    print("Substraction is :", Ret)
    
    Ret = obj4.Multiplication()
    print("Multiplication is :", Ret)
    
    Ret = obj4.Division()
    print("Division is :", Ret)
    
    
    
if __name__ == "__main__":
    main()