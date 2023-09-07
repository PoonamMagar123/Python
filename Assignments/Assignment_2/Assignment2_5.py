
def main():
    Value = int(input("Enter a number : "))
    
    flag = True
    for i in range(2,Value):
        if Value % i == 0:
            flag = False

    if flag == True:
        print("It is Prime Number")  
    else:
        print("It is Not Prime Number")
   
if __name__ == "__main__":
    main()