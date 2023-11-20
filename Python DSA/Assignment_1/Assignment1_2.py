

def main():
    
    my_list = [1, '2050', 'hello', 50, 'python', 2006]

    new_list = []

    for i in my_list:
        if not isinstance(i, int):
            new_list.append(i)

    print(new_list)
            
    
if __name__ == "__main__":
    main()