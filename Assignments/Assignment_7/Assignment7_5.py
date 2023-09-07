import threading
          
def Even(no):
    print("Displaying  1 to 50  : ")
    
    for i in range(1,no + 1):
        print(i, end=" ")
    
def Odd(no):
    print("\n Displaying  1 to 50 in reverse Order : ")
    
    for i in range(no,0,-1):
        print(i, end=" ")
                       
def main():
    Num = 50
    
    tread1 = threading.Thread(target=Even, args=(Num,))
    
    tread2 = threading.Thread(target=Odd, args=(Num,))

    tread1.start()
    tread1.join()
    
    tread2.start()
    tread2.join()
    
if __name__ == "__main__":
    main()