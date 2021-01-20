# Import OS and CSV reader modules
import os
import csv

# Describe file path to CSV file
election_csv = os.path.join('Resources', 'election_data.csv')

# What are the elements I am trying to calculate? with election_data as sole parameter
def election_results(election_data):
    #candidate = str(election_data[2])
    vote_count = int()

#Set up to read csv
with open(election_csv, 'r') as election_data:

    #split by commas
    csvreader = csv.reader(election_data, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Many thanks to Beau Jeffrey for sharing how he simplified
    #construction of the candidate dictionary

    total_votes = 0
    winner = 0
    candidate_dict = {}
    percent_dict = {}

    for row in csvreader:

        candidate = row[2]
        total_votes += 1
        votes = {}

        if candidate not in candidate_dict:
            candidate_dict[candidate] = 1

        else:
            candidate_dict[candidate] += 1

    print(candidate_dict)
    # Print the first actor
    print(f'{candidate_dict["candidate"][0]}')





# Final display
print("Election Results")
print("-------------------")
print("Candidate 1 name: percentage count")
print("Candidate 2 name: percentage count")
print("Candidate 3 name: percentage count")
print("Candidate 4 name: percentage count")
print("-------------------")
print("Winner: Candidate that wins")
print("-------------------")






# Establish one function to calculate all election results
# with 'election_data' as the sole parameter
# def election_results(election_data):

#     # What elements do I need to work with?
#     candidate = unique name as appears in column [2]
#     total_votes = number of rows
#     candidate_vote_count = number of appearances of each name in column [2]
#     winner = candidate with highest candidate_vote_count











   





    

