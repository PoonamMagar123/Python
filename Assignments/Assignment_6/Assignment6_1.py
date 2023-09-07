class BookStore:
    NOofBooks = 0
    
    def __init__(self,Name,Author):
        self.name = Name
        self.author = Author
        
    def Display(self):
        BookStore.NOofBooks += 1
        print(self.name , "by", self.author,". No Of Book : " ,BookStore.NOofBooks)

def main():
    Value1 = input("Enter Name of Book : ")
    Value2 = input("Enter Author : ")
    
    obj1 = BookStore(Value1,Value2)
    obj1.Display()
    
    Value1 = input("Enter Name of Book : ")
    Value2 = input("Enter Author : ")
    
    obj2 = BookStore(Value1,Value2)
    obj2.Display()
        
if __name__ == "__main__":
    main()