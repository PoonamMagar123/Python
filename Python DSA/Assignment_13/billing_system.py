class Node():
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
        
class Queue():
    def __init__(self):
        self.front = None
        self.Rear = None
        self.count = 0

    def is_empty(self):
        return self.front == None

    def enqueue(self, data):
        n = Node(data)
        if not self.is_empty():
            start.Rear = n
        self.count += 1
        return data
        
    def dequeue(self):
        if not self.is_empty(): 
            self.Rear == self.front == None
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
        return self.count

# Example usage
if __name__ == "__main__":
    mylist = Queue()
    mystack1 = mylist.enqueue(10)
    mystack2 = mylist.enqueue(20)
    mystack3 = mylist.enqueue(30)
    print(mystack1)
    print(mystack2)
    print(mystack3)
    print("Queue size:", mylist.size()) 
    print("Dequeue element in list :",mylist.dequeue())

    # print("Queue size after remove front element is:" ,mylist.size())           # Output: 3
    # print("Front element:", mylist.get_front())         
    # print("Rear element:", mylist.get_rear()) 
