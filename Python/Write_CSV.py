# Read more: https://realpython.com/python-csv/
# https://medium.com/@robblatt/use-python-and-pandas-to-append-to-a-csv-503bf22670ce
# https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/

import pandas as pd
#from pandas import read_csv
import csv

filename = 'write_test.csv'

# Use module 'pandas'
# Mode: w = write, a = append, a+ = append in newline
def write_csv_by_Pandas(file):
    df = pd.DataFrame({'TIME':['2010','2011'],
                   'GEO':['Serbia','Serbia'],
                   'UNIT':['Euro','Euro'],
                   'NA_ITEM':['Compensation of employees per hour worked','Compensation of employees per hour worked'],
                   'Value':[':',':'],
                   'Flag and Footnotes':['','']})

    df.to_csv('write_test.csv', mode = 'a+', header = False, quotechar='"', quoting=csv.QUOTE_ALL, index=False)


# Use built-in 'csv'
def write_csv(file):
    with open(file, mode='a', newline='\n', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        writer.writerow([2012,"Serbia","Euro","Compensation of employees per hour worked",":",""])
        writer.writerow([2013,"Serbia","Euro","Compensation of employees per hour worked",":",""])

# Use built-in 'csv' (dict)
def write_csv_with_dict(file):
    with open(file, mode='a', newline='\n', encoding='utf-8') as csv_file:
        fieldnames = ['TIME', 'GEO', 'UNIT','NA_ITEM','Value','Flag and Footnotes'] 
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        #writer.writeheader()
        writer.writerow({"TIME":2014, "GEO":"Serbia", "UNIT":"Euro", "NA_ITEM": "Compensation of employees per hour worked", "Value":":", "Flag and Footnotes":""})



def main():
    print("\n[A. Pandas]")
    write_csv_by_Pandas(filename)
    print("\n[B. Python Built-in]")
    write_csv(filename)
    print("\n[C. Python Built-in (Dict)]")
    write_csv_with_dict(filename)

if __name__ == "__main__":
    main()