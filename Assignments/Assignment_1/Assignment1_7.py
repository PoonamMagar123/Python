def CheckNum(No):
    if(No % 5 == 0):
        return True
    else:
        return False

Num = int(input("Enter a number: "))

Isdivisible = CheckNum(Num)
print(Isdivisible)
    

