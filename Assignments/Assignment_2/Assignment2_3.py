
def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def main():
        num = int(input("Enter a number: "))
        
        factors = get_factors(num)
        factors_sum = 0
        for factor in factors:
            factors_sum += factor
        print("Factors of Number:", factors)
        print("Sum of factors:", factors_sum)

if __name__ == "__main__":
    main()
