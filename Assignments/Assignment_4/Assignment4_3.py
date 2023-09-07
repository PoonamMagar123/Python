from functools import reduce

#lambda function 

check = lambda No : No >= 70 and No <= 90

Increase = lambda No : No + 10

Product = lambda A,B : A * B

def main():
    Data = []
    
    Value = int(input("Enter Number : "))
    
    for i in range(Value):
        num = int(input())
        Data.append(num)
    
    print("Entered Numbers : ",Data)
    
    filteroutput = list(filter(check,Data))
    print("Numbers are greater than or eqaul to 70 & less than equal to 90 : ",filteroutput)
    
    mapout = list(map(Increase,filteroutput))
    print("Numbers are increased by 10 : ",mapout)
    
    reduceout = reduce(Product,mapout)
    print("Product of that numbers : ",reduceout)
    
if __name__ == "__main__":
    main()