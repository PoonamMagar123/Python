class Node:
    def __init__(self,prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DequeueDLL():
    def __init__(self):
        self.front = None  
        self.rear = None

    def is_empty(self):
        return self.front == None

    def insert_front(self, data):
        n = Node(None, data, self.front)
        if not self.is_empty():
            self.front.prev=n
        self.front=n
        return data

    def insert_rear(self, data):
        temp=self.rear
        if self.rear is not None:
            while temp.next != None:
                temp=temp.next
        n = Node(temp, data, None)
        if temp == None:
            self.rear=n
        else:
            temp.next=n

    # def delete_front(self):
    #     if not self.is_empty():
            
    #     else:
    #         raise IndexError("Dequeue is empty")

    # def delete_rear(self):
    #     if not self.is_empty():
    #         return self.rear.item
    #     else:
    #         raise IndexError("Dequeue is empty")

    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Dequeue is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Dequeue is empty")

    def size(self):
        return len(self.Dequeuelist)

# Example usage
if __name__ == "__main__":
    mylist = DequeueDLL()
    print(mylist.insert_front(10))
    mylist.insert_front(20)
    mylist.insert_front(30)
    mylist.insert_front(40)
    mylist.insert_front(50)
    mylist.insert_rear(90)
    mylist.insert_rear(60)
    mylist.insert_rear(70)

    # print("Dequeue size:", mylist.size())
    # print("Delete front element in list:", mylist.delete_front())
    # print("Delete rear element in list:", mylist.delete_rear())
    # print("Dequeue size after remove  elements is:", mylist.size())  # Output: 2
    
    print("Front element:", mylist.get_front())
    print("Rear element:", mylist.get_rear())
