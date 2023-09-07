import threading
          
def Even(No):
    print("Addition of Even Number in list : ")
    
    sum = 0
    for factor in No:
        if(factor % 2 == 0):
            sum += factor
    print(sum)
            
            
def Odd(No):
    print("Addition of Odd Number in list : ")
  
    sum = 0
    for factor in No:
        if(factor % 2 != 0):
            sum += factor
    print(sum)
                       
def main():
    Num = int(input("Enter a Number: "))
    Arr = []
    
    for i in range(Num):
        value = int(input())
        Arr.append(value)
    
    print(Arr)
    
    EvenList = threading.Thread(target=Even, args=(Arr,))
    
    OddList = threading.Thread(target=Odd, args=(Arr,))

    EvenList.start()
    EvenList.join()
    
    OddList.start()
    OddList.join()
    
if __name__ == "__main__":
    main()