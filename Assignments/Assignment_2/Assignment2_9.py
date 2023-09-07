
def main():
    i = int(input("Enter a number : "))
    
    Count = 0
    
    while (i != 0):
        
        i = i // 10
        
        Count = Count + 1
        
    print("Length of digit",str(Count))
    
   
if __name__ == "__main__":
    main()