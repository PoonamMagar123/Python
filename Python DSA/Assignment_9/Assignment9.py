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
 

    
