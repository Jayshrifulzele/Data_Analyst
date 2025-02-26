import csv

with open (file="DID.csv", mode="r") as file:
    csv_reader = csv.reader(file)

    #read only the column keys and generate array of its
    header = next(csv_reader)
    print("Header:",header)

    #iterate each row and column
    for row in csv_reader:
        print(row)