class Queue():
    def __init__(self):
        self.Queue = []

    def is_empty(self):
        return len(self.Queue) == 0

    def enqueue(self, data):
        self.Queue.append(data)
        return data
        
    def dequeue(self):
        if not self.is_empty(): 
            return self.Queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def get_front(self):
        if not self.is_empty():
            return self.Queue[0]
        else:
            raise IndexError("Queue is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.Queue[-1]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.Queue)

# Example usage
if __name__ == "__main__":
    mylist = Queue()
    mystack1 = mylist.enqueue(10)
    mystack1 = mylist.enqueue(20)
    mystack1 = mylist.enqueue(30)

    print("Queue size:", mylist.size()) 
    print("Dequeue element in list :",mylist.dequeue())

    print("Queue size after remove front element is:" ,mylist.size())           # Output: 3
    print("Front element:", mylist.get_front())         
    print("Rear element:", mylist.get_rear()) 
