
            
def main():
    
    value = int(input("Enter a number"))

    Arr = list()

    print("Enter element: ")

    for i in range(value):
        num = int(input())
        Arr.append(num)
        
    max_value = Arr[0]

    for No in Arr:
        if No > max_value:
            max_value = No

    print("Maximum Number in the list:", max_value)

if __name__ == "__main__":
    main()
    