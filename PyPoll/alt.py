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

    #stuff below thanks to beau

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

  







    # vote_khan = 0
    # vote_correy = 0
    # vote_li = 0
    # vote_otooley = 0
    
    # # could I do a while loop starting with an empty variable 'active_candidate'?
    # # candidate = []
    # #while candidate == "this is where I don't know how to execute"
    #     #put active candidate into dictionary as a value to key of Candidate
    #     #if candidate == the next row, then
    #         #add to the counter for that candidate
    #         #append candidate name to list of candidates?
    #         #use list to create dictionary
    #             #maybe no?
    #         #produce results based on dictionary???


    # for candidate in csvreader:
    #     if candidate[2] == 'Khan':
    #         vote_khan += 1

    #     elif candidate[2] == 'Correy':
    #         vote_correy += 1

    #     elif candidate[2] == 'Li':
    #         vote_li += 1

    #     elif candidate[2] == "O'Tooley":
    #         vote_otooley += 1

    # #This works below the counter but not above. Weird.
    # # total_votes = len(list(csvreader)

    
    # print("The vote count for Khan is")
    # print(vote_khan) 
    



   

