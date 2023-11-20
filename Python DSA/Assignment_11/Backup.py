# import os

# def backup_phone():
#     # Run ADB commands to backup the phone
#     if(os.system('adb devices')):  # Check if the device is connected
#         print("Backup is successfully...")
#     os.system('adb backup -apk -shared -all -f backup.ab')

# if __name__ == "__main__":
#     backup_phone()
# my_ints = [4, 6, 3, 9, 2, 8, 12]
# for i in my_ints:
#     if i <= 7:
#         print(i)

# Sample list of numbers
numbers = [10, 20, 30, 40, 50, 60, 68]

# Calculate the length of the list
length = len(numbers)

# Calculate the middle index (or indices)
middle_index = length // 2

# Retrieve the middle number(s) from the list
if length % 2 == 0:   # If the list has an even number of elements
    middle_number1 = numbers[middle_index - 1]
    middle_number2 = numbers[middle_index]
    print("Middle numbers in the list (even number of elements):", middle_number1, middle_number2)
else: # If the list has an odd number of elements
    middle_number = numbers[middle_index]
    print("Middle number in the list (odd number of elements):", middle_number)