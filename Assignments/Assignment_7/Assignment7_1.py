import threading
          
def Even(No):
    print("First 10 Even Number : ")
    for i in range(2,No,2):
            print(i)
            
def Odd(No):
    print("First 10 Odd Number : ")
    for i in range(1,No,2):
            print(i)
                       
def main():
    Num = 20
    
    p1 = threading.Thread(target=Even, args=(Num,))
    
    p2 = threading.Thread(target=Odd, args=(Num,))

    p1.start()
    p1.join()
    
    p2.start()
    p2.join()
    
if __name__ == "__main__":
    main()