class Heap():
    def __init__(self):
        self.heap = []

    def create_heap(self, list1):
        for e in list1:
            self.insert(e)

    def insert(self, e):
        index = len(self.heap)
        parentIndex = (index-1)//2
        while index>0 and self.heap[parentIndex]<e:
            if index==len(self.heap):
                self.heap.append(self.heap[parentIndex])
            else:
                self.heap[index]=self.heap[parentIndex]
            index = parentIndex
            parentIndex = (index-1)//2
        
        if index == len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index] = e

    def top(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        return self.heap[0]
    
    def delete(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        if len(self.heap)==1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        temp = self.heap.pop()
        index = 0
        leftchildIndex = 2*index+1
        rightchildIndex = 2*index+1

        while leftchildIndex<len(self.heap):
            if rightchildIndex<len(self.heap):
                if self.heap[leftchildIndex]>self.heap[rightchildIndex]:
                    if self.heap[leftchildIndex]>temp:
                        self.heap[index]=self.heap[leftchildIndex]
                        index = leftchildIndex
                    else:
                        break
                else:
                    if self.heap[rightchildIndex]>temp:
                        self.heap[index] = self.heap[rightchildIndex]
                        index = rightchildIndex
                    else:
                        break
            else: # No Right Child
                if self.heap[leftchildIndex]>temp:
                    self.heap[index]=self.heap[leftchildIndex]
                    index=leftchildIndex
                else:
                    break
            leftchildIndex=2*index+1
            rightchildIndex=2*index+2
        
        self.heap[index] = temp
        return max_value
    
    def heapSort(self, list1):
        self.create_heap(list1)
        list2 = []
        try:
            while True:
                list2.insert(0, self.delete())
        except EmptyHeapException:
            pass
        return list2

class EmptyHeapException(Exception):
    def __init__(self, msg="Empty Heap"):
        self.msg = msg
    
    def __str__(self):
        return self.msg
 

def main():
    list1 = [34, 56, 12, 78, 10]
    mylist = Heap()
    l = mylist.heapSort(list1)
    print(l)


if __name__ == "__main__":
    main()
                