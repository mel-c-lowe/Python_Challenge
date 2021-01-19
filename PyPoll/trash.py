# Import OS and CSV reader modules
import os
import csv

# Describe file path to CSV file
election_csv = os.path.join('Resources', 'election_data.csv')

#Set up to read csv
with open(election_csv, 'r') as election_data:

    #split by commas
    csvreader = csv.reader(election_data, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    candidates = election_data[2]
    for candidate in candidates:
        print(candidate)