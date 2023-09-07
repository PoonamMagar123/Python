         
def main():
    
    Number = int(input("Enter a number"))

    Arr = list()

    print("Enter element: ")

    for i in range(Number):
        num = int(input())
        Arr.append(num)
        
    min_value = Arr[0]

    for No in Arr:
        if No < min_value:
            min_value = No

    print("Minimum Number in the list:", min_value)

if __name__ == "__main__":
    main()
    