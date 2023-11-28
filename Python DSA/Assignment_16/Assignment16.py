class PriorityQueue:
    def __init__(self):
        self.items=[]

    def push(self, data, priority):
        index = 0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index, (data,priority))
    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty")
        return self.items.pop(0)[0]

def main():
    priorityQ = PriorityQueue()
    priorityQ.push('Amit' ,3)
    priorityQ.push('Amar' ,1)
    priorityQ.push('Anand' ,2)

    while not priorityQ.is_empty():
        print(priorityQ.pop())

if __name__ == "__main__":
    main()



