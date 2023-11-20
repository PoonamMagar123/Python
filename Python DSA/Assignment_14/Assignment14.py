class Dequeue():
    def __init__(self):
        self.Dequeuelist = []

    def is_empty(self):
        return len(self.Dequeuelist) == 0

    def insert_front(self, data):
        self.Dequeuelist.insert(0, data)
        return data

    def insert_rear(self, data):
        self.Dequeuelist.append(data)
        return data

    def delete_front(self):
        if not self.is_empty():
            return self.Dequeuelist.pop()
        else:
            raise IndexError("Dequeue is empty")

    def delete_rear(self):
        if not self.is_empty():
            return self.Dequeuelist.pop(0)
        else:
            raise IndexError("Dequeue is empty")

    def get_front(self):
        if not self.is_empty():
            return self.Dequeuelist[0]
        else:
            raise IndexError("Dequeue is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.Dequeuelist[-1]
        else:
            raise IndexError("Dequeue is empty")

    def size(self):
        return len(self.Dequeuelist)

# Example usage
if __name__ == "__main__":
    mylist = Dequeue()
    mylist.insert_front(10)
    mylist.insert_front(20)
    mylist.insert_front(30)
    mylist.insert_rear(40)
    mylist.insert_rear(50)
    print("Dequeue size:", mylist.size())
    print("Delete front element in list:", mylist.delete_front())
    print("Delete rear element in list:", mylist.delete_rear())
    print("Dequeue size after remove  elements is:", mylist.size())  # Output: 2
    
    print("Front element:", mylist.get_front())
    print("Rear element:", mylist.get_rear())
