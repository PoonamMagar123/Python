
def main():
    
    my_list = [1,2,446,67,8,989]

    
    Sum = 0
    for i in my_list:
        Sum += i
        Res = Sum / len(my_list)
      
    print(Res)      
    
if __name__ == "__main__":
    main()