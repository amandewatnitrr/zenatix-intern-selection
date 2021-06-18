from csv import reader

with open('bmp_180.csv', 'r', encoding='UTF8') as f:
    csv_reader = reader(f)
    row =csv_reader
    for row in csv_reader:
        print(row)