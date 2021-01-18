# Import OS and CSV reader modules
import os
import csv

# Describe file path to CSV file
election_csv = os.path.join('Resources', 'election_data.csv')

# What are the elements I am trying to calculate? with election_data as sole parameter
def election_results(election_data):
    candidate = str(election_data[2])
    vote_count = int()



#Set up to read csv
with open(election_csv, 'r') as csvfile:

    #split by commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    ctr = 0
    for candidate in csvreader:
        if candidate[2] == 'Khan':
            ctr += 1
    print(ctr)
