def insert_sort(data_list):
    for r in range(1, len(data_list)):
        for i in range(len(data_list)-r):
            if data_list[i] > data_list[i+1]:
                data_list[i],data_list[i+1] = data_list[i+1],data_list[i]

def main():
    l = [34, 67, 89, 25, 50]
    insert_sort(l)
    print(l)
    modified_insert_sort(l)
    print(l)

if __name__ == "__main__":
    main()