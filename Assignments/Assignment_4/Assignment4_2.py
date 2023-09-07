#lambda function 
fun_Mult = lambda No1,No2 : (No1 * No2)

def main():
    
    Value1 = int(input("Enter First Number : "))
    
    Value2 = int(input("Enter Second Number : "))
    
    Mult = fun_Mult(Value1,Value2)
    
    print("Multiplication of given number:",Mult)
    
if __name__ == "__main__":
    main()