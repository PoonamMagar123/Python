 #1: Find the length of the list and simply swap the first element with (n-1)th element.
def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList

# Approach #2: The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with list[-1].
def swapList1(newList):

    newList[0] , newList[-1] = newList[-1], newList[0]
    return newList

# Approach #3: Swap the first and last element is using tuple variable. Store the first and last element as a pair in a tuple variable, say get, and unpack those elements with first and last element in that list. Now, the First and last values in that list are swapped.
 
def swapList2(List):
    get = List[-1], List[0]
    List[0], List[-1] = get

    return List

def main():
    newList = [12, 35, 9, 56, 24]

    print(swapList(newList))

    newList1 = [12, 35, 9, 56, 24]

    print(swapList1(newList1))

    newList2 = [13, 35, 9, 56, 20]

    print(swapList2(newList2))
if __name__ == "__main__":
    main()