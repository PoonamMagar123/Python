import csv

def create_table(value, filename):
    rows = []

    for i in range(1, 10+1):
        res = value * i
        rows.append([str(res)])

    with open(filename, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)

def main():
    value = int(input("Enter a number: "))

    file = input("Enter a file name: ")
    create_table(value, file)
    print("saved successfully")

if __name__ == "__main__":
    main()

