# Read more: https://realpython.com/python-csv/

import pandas as pd
#from pandas import read_csv
import csv

filename = 'read_test.csv'

# Use module 'pandas'
def read_csv_by_Pandas(file):
    # 'sep' (optional) indicates the delimiter, default ','
    # 'header' (optional) indicates the header line number, default '0'
    # More: https://honingds.com/blog/pandas-read_csv/
    df = pd.read_csv(file, sep=",", header=0) 
    print(df.head(2))
    print(df.head(3)['TIME'])

# Use built-in 'csv'
def read_csv(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column: {", ".join(row)}')
                line_count += 1
            elif line_count == 3:
                break
            else: 
                print(f'\t{row[0]}, {row[1]}, {row[2]}, {row[3]}')
                line_count += 1
            
        print(f'Processed {line_count} lines.')

# Use built-in 'csv' (dict)
def read_csv_as_dict(file):
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column: {", ".join(row)}')
                line_count += 1
            if line_count == 3:
                break
            print(f'\t{row["TIME"]}, {row["GEO"]}, {row["NA_ITEM"]}, {row["Value"]}')
            line_count += 1
        print(f'Processed {line_count} lines.')




def main():
    print("\n[A. Pandas]")
    read_csv_by_Pandas(filename)
    print("\n[B. Python Built-in]")
    read_csv(filename)
    print("\n[C. Python Built-in (Dict)]")
    read_csv_as_dict(filename)

if __name__ == "__main__":
    main()
