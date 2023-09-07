import threading
          
def Even(No):
    print("Addition Even Factors of {} : ".format(No))
    factors = []
    for i in range(2,No,2):
            factors.append(i)
           
    sum = 0
    for factor in factors:
        sum += factor
        
    print(sum)
            
            
def Odd(No):
    print("Addition Odd Factors of {} : ".format(No))
    factors = []
    for i in range(1,No,2):
            factors.append(i)
    
    sum = 0
    for factor in factors:
        sum += factor
        
    print(sum)
                       
def main():
    Num = int(input("Enter a Number: "))
    
    EvenFactors = threading.Thread(target=Even, args=(Num,))
    
    OddFactors = threading.Thread(target=Odd, args=(Num,))

    EvenFactors.start()
    EvenFactors.join()
    
    OddFactors.start()
    OddFactors.join()
    
if __name__ == "__main__":
    main()