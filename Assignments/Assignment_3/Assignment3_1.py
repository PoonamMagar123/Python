
value = int(input("Enter a number :"))

Arr = list()

print("Enter element: ")
for i in range(value):
    num = int(input())
    Arr.append(num)
    
sumOfElements = 0
for element in Arr:
    sumOfElements = sumOfElements + element
    

print("Sum of all the elements in the list is:", sumOfElements)
    
    