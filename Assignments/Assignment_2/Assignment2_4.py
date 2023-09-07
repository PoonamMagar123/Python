def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
        
fact = int(input("enter the number : "))
print(factorial(fact))

sum = 0
sum = sum + fact
print("Sum of factorial number: ",sum)