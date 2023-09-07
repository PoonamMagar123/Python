from functools import reduce

#lambda function 

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def mapX(x,y):
    x = 0
    if(x > y):
        return x
    else:
        return y
    #return x if x > y else y
       
def main():
    Data = []
    
    Value = int(input("Enter Number : "))
    
    for i in range(Value):
        num = int(input())
        Data.append(num)
    
    print("Entered Element : ",Data)
    
    filteroutput = list(filter(is_prime,Data))
    print("Prime Numbers : ",filteroutput)
    
    mapout = list(map(lambda No : (No * 2),filteroutput))
    print("Multiply each number by 2 : ",mapout)
    
    reduceout = reduce(mapX,mapout)
    print("maximum number of list : ",reduceout)
    
if __name__ == "__main__":
    main()