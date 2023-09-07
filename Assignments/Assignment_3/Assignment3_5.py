import MarvellousNum

def ListPrime(numbers):
    prime_sum = 0
    for num in numbers:
        if MavellousNum.Chkprime(num):  # Call the Chkprime function from the user-defined module
            prime_sum += num
    return prime_sum

def main():
    
        n = int(input("Enter the number of elements: "))
        num_list = []
        for i in range(n):
            num = int(input("Enter element: "))
            num_list.append(num)

        prime_sum = ListPrime(num_list)
        print("Sum of prime numbers:", prime_sum)

if __name__ == "__main__":
    main()

    