
def calculate_frequency(numbers, target):
    frequency = 0
    for num in numbers:
        if num == target:
            frequency += 1
    return frequency

def main():
  
        num_count = int(input("Enter the number of elements: "))
        numbers = list()

        print("Enter number : ")
        
        for i in range(num_count):
            num = int(input())
            numbers.append(num)

        target_number = int(input("Search Element : "))
        
        frequency = calculate_frequency(numbers, target_number)
        print("The frequency of number is : ",frequency)


if __name__ == "__main__":
    main()
