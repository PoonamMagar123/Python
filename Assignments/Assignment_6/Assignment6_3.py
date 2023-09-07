class Numbers:
    
    def __init__(self,Value):
        self.value = Value
        print("The Number Is : ",self.value)
        
    def ChkPrime(self):
        if self.value <= 1 or self.value == 0:
            return False
        for i in range(2,self.value):
            if self.value % i == 0:
                return False
            return True
        
    def ChkPerfect(self):
        sum = 0
        for i in range(1,self.value):
            if(self.value % i == 0):
                sum += i
        if(sum == self.value):
            return True
        else:
            return False
        
    def Factors(self):
        factors = []
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                factors.append(i)
        
        factors_sum = 0
        for i in factors:
            factors_sum += i
        return factors_sum
     
        
def main():
    No = int(input("Enter A Number : "))
    
    obj1 = Numbers(No)
    
    print("Is the given number a Prime Number? (True/False) : ",obj1.ChkPrime())
    
    print("Is the given number a Perfect Number? (True/False) : ",obj1.ChkPerfect())
    
    print("Sum of all factors in given number is  : ",obj1.Factors())
    
    
    No = int(input("Enter A Number : "))
    
    obj2 = Numbers(No)
    
    print("Is the given number a Prime Number? (True/False) : ",obj2.ChkPrime())
    
    print("Is the given number a Perfect Number? (True/False) : ",obj2.ChkPerfect())
    
    print("Sum of all factors in given number is : ",obj2.Factors())
    
    
if __name__ == "__main__":
    main()   