class Stack(list):
    def is_empty(self):
        return len(self) == 0
        
    def push(self, item):
        return self.append(item)          
        
    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            return super().pop()
        
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self[-1]
        
    def size(self):
        return len(self)
    
    def insert(self, index, data):
        raise AttributeError("No attribute 'insert' in stack")
    
def main():
    mylist = Stack()
    mystack1 = mylist.push(10)
    
    
    print(mylist.push(20))
    print(mylist.push(50))
    print(mylist.push(60))
    print(mylist)
    # poplist = mylist.pop()
    # print(poplist)
    
    peeklist = mylist.peek()
    print(peeklist)
if __name__ == "__main__":
    main()
        