def natural_numbers(n):
    # Recursively prints the first n natural numbers in ascending order.
    if n > 0:
        natural_numbers(n-1)
        print(n, end=' ')

def natural_numbers_reverse(n):
    # Recursively prints the first n natural numbers in descending order.
    if n > 0:
        print(n, end=' ')
        natural_numbers_reverse(n-1)

def natural_numbers_odd(n):
    # Recursively prints the first n odd natural numbers in ascending order.
    if n > 0:
        natural_numbers_odd(n-1)
        print(2*n-1, end=' ')

def natural_numbers_even(n):
    # Recursively prints the first n even natural numbers in ascending order.
    if n > 0:
        natural_numbers_even(n-1)
        print(2*n, end=' ')

def natural_numbers_odd_reverse(n):
    # Recursively prints the first n odd natural numbers in descending order.
    if n > 0:
        print(2*n-1, end=' ')
        natural_numbers_odd_reverse(n-1)

def natural_numbers_even_reverse(n):
    # Recursively prints the first n even natural numbers in descending order.
    if n > 0:
        print(2*n, end=' ')
        natural_numbers_even_reverse(n-1)

def main():
    print("Natural Numbers:")
    natural_numbers(5)

    print("\nNatural Numbers Reverse:")
    natural_numbers_reverse(5)

    print("\nNatural Numbers Odd:")
    natural_numbers_odd(5)

    print("\nNatural Numbers Even:")
    natural_numbers_even(5)

    print("\nNatural Numbers Odd Reverse:")
    natural_numbers_odd_reverse(5)

    print("\nNatural Numbers Even Reverse:")
    natural_numbers_even_reverse(5)
if __name__ == "__main__":
    main()
