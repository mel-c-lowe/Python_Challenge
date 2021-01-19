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
with open(election_csv, 'r') as election_data:

    #split by commas
    csvreader = csv.reader(election_data, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    vote_khan = 0
    vote_correy = 0
    vote_li = 0
    vote_otooley = 0
    for candidate in csvreader:
        if candidate[2] == 'Khan':
            vote_khan += 1

        elif candidate[2] == 'Correy':
            vote_correy += 1

    
    print("The vote count for Khan is")
    print(vote_khan)
    print("The vote count for Correy is")
    print(vote_correy)
