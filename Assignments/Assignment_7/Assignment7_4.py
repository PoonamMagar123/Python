import threading
import os
          
def Capital(No):
    print("Thread ID of Capital thread is : ",threading.get_ident())
    print("Number of capital character : ")
    Caps_Char = ""
    for char in No:
        if char.isupper():
            Caps_Char += char
    print(len(Caps_Char))
    
def Small(No):
    
    print("Thread ID of Small thread is : ",threading.get_ident())
    print("Number of Small character : ")
    Small_char = ""
    for char in No:
        if char.islower():
            Small_char += char
    print(len(Small_char))
    
def Digit(No):
    
    print("Thread ID of Digit thread is : ",threading.get_ident())
    print("Number of Digit  : ")
    number = ""
    for num in No:
        if num.isdigit():
            number += num
    print(len(number))
            
def main():
    Num = input("Enter a String : ")
    
    print("Thread ID of main thread is : ",threading.get_ident())
    
    capital = threading.Thread(target=Capital, args=(Num,))
    
    small = threading.Thread(target=Small, args=(Num,))
    
    digit = threading.Thread(target=Digit, args=(Num,))

    capital.start()
    capital.join()
    
    small.start()
    small.join()
    
    digit.start()
    digit.join()
    
if __name__ == "__main__":
    main()