from functools import reduce

#lambda function 

chechEven = lambda No : No % 2 == 0

sqaure = lambda No : (No * No)

Add = lambda A,B : A + B

def main():
    Data = []
    
    Value = int(input("Enter Number : "))
    
    for i in range(Value):
        num = int(input())
        Data.append(num)
    
    print("Entered Element : ",Data)
    
    filteroutput = list(filter(chechEven,Data))
    print("Even Numbers : ",filteroutput)
    
    mapout = list(map(sqaure,filteroutput))
    print("Square of the even numbers : ",mapout)
    
    reduceout = reduce(Add,mapout)
    print("Addition of that number : ",reduceout)
    
if __name__ == "__main__":
    main()