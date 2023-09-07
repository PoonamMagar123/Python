import Arithmatic

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter Second number: "))
        
    Result = Arithmatic.Add(Value1,Value2)
    print("Addition is :",Result)
    
    Result = Arithmatic.Sub(Value1,Value2)
    print("Substraction is :",Result) 
    
    Result = Arithmatic.Mult(Value1,Value2)
    print("Multiplication is :",Result) 
    
    Result = Arithmatic.Div(Value1,Value2)
    print("Division is :",Result) 
    
if __name__ == "__main__":
    main()
	