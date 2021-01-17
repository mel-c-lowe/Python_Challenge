# Import OS and CSV reader modules
import os
import csv

# Describe file path to CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

# Make the CSV reader

with open(csvpath) as csvfile: 

    # Describe the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    # Make sure that worked
    # Great! At least the header is working
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    vote_count = len(list(csvreader))
    print("The total number of votes is")
    print(vote_count)



    

