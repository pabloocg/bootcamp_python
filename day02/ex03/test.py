from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        if file == None:
            print("File is corrupted")
        data = file.getdata()
        header = file.getheader()
    for elem in data:
        print(elem)
    print(header)
    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted")