#lambda function 
fun_power = lambda No : (No * No)

def main():
    
    print("Enter Number : ")
    Value = int(input())
    
    power = fun_power(Value)
    print("Power of The Given number:",power)
    
if __name__ == "__main__":
    main()