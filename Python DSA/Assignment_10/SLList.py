class Node():
    
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList():
    def __init__(self):
        self.start = None
        
    def is_empty(self):
        return self.start == None
        
    def push(self, data):
        N = Node(data)
        if not self.is_empty():
            N.next = self.start
        self.start = N
        return data
                 
    def pop(self):
        if not self.is_empty():
            popped_node = self.start
            self.start = self.start.next
            popped_node.next = None
            return popped_node.data
        else:
            raise IndexError("stack is empty")
        
    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            return self.start.data
        
    def size(self):
        current = self.start
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
# def main():
#     mylist = Stack()
#     print(mylist.push(10))
#     print(mylist.push(20))
#     print(mylist.push(50))
#     print(mylist.push(60))
    
#     print("Size of stack : ",mylist.size())
#     poplist = mylist.pop()
#     print("poped item : ",poplist)
#     peeklist = mylist.peek()
#     print("Top item : ",peeklist)
#     print("Size of stack after poped : ",mylist.size())
   
# if __name__ == "__main__":
#     main()
    
