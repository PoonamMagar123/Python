class Stack:
    
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0
        
    def push(self, item):
        return self.stack.append(item)          
        
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.stack.pop()
        
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.stack[-1]
        
    def size(self):
        return len(self.stack)
    
def main():
    mylist = Stack()
    mystack1 = mylist.push(10)
    
    print(mylist)
    print(mylist.push(20))
    print(mylist.push(50))
    print(mylist.push(60))
    
    # poplist = mylist.pop()
    # print(poplist)
    
    peeklist = mylist.peek()
    print(peeklist)
if __name__ == "__main__":
    main()
        