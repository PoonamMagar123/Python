def sum_natural_numbers(n):
    if n <= 1:
        return n
    else:
        return n + sum_natural_numbers(n-1)

def natural_numbers_sum_even(n):
    if n == 1:
        return 2
    else:
        return 2*n + natural_numbers_sum_even(n-1)

def natural_numbers_sum_odd(n):
    if n == 1:
        return 1
    else:
        return 2*n-1 + natural_numbers_sum_odd(n-1)

def natural_numbers_square_sum(n):
    if n == 1:
        return 1
    else:
        return n * n + natural_numbers_square_sum(n-1)

def natural_numbers_factorial_sum(n):
    if n == 1:
        return 1
    else:
        return n * natural_numbers_factorial_sum(n-1)

def main():
    print("Sum Of Natural Numbers:", sum_natural_numbers(10))
    print("\nSum Of Even Natural Numbers :", natural_numbers_sum_even(10))
    print("\nSum Of Odd Natural Numbers :", natural_numbers_sum_odd(10))
    print("\nSum Of Factorial Natural Numbers :", natural_numbers_factorial_sum(10))
    print("\nSum Of Sqaure of Natural Numbers :", natural_numbers_square_sum(10))

if __name__ == "__main__":
    main()
