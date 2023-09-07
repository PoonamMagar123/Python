
def main():
    i = int(input("Enter a number : "))
    
    sum = 0
    
    while (i > 0):
        sum = sum + i%10
        
        i = i // 10
        
    print("Sum of digit",sum)
    
   
if __name__ == "__main__":
    main()