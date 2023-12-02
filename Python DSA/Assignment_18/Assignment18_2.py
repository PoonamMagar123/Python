def GCD(num1, num2):
    if num2 == 0:
        return num1
    else:
        return (GCD(num2, num1%num2))
def main():
    NO1 = int(input("Enter a number : "))
    NO2 = int(input("Enter a number : "))
    r = GCD(NO1, NO2)
    print(r)
if __name__ == "__main__":
    main()