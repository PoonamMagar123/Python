# DSA using Python
# Assignment-10: Stack using Linked List
# 1. Import module containing singly linked list code in your python file.
# 2. Define a class Stack to implement stack data structure. Define _init_() method to create Singly Linked List (SLL) object.
# 3. Define a method is_empty() to check if the stack is empty in Stack class.
# 4. In Stack class, define push() method to add data onto the stack.
# 5. In Stack class, define pop() method to remove top element from the stack.
# 6. In Stack class, define peek() method to return top element on the stack.
# 7. In Stack class, define size() method to return size of the stack that is number of items present in the stack.

from SLList import SinglyLinkedList

class Stack1:
    def __init__(self):
        self.sll = SinglyLinkedList()

    def is_empty(self):
        return self.sll.is_empty()

    def push(self, data):
        self.sll.push(data)

    def pop(self):
        return self.sll.pop()

    def peek(self):
        return self.sll.peek()

    def size(self):
        return self.sll.size()

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack is empty:", stack.is_empty())  # Output: False
    print("Stack size:", stack.size())           # Output: 3
    print("Top element:", stack.peek())           # Output: 3

    popped_item = stack.pop()
    print("Popped element:", popped_item)        # Output: 3
    print("Stack size after pop:", stack.size())  # Output: 2
 

    
