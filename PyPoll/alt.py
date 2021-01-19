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
    
    # could I do a while loop starting with an empty variable 'active_candidate'?
    # candidate = []
    #while candidate == "this is where I don't know how to execute"
        #put active candidate into dictionary as a value to key of Candidate
        #if candidate == the next row, then
            #add to the counter for that candidate


    for candidate in csvreader:
        if candidate[2] == 'Khan':
            vote_khan += 1

        elif candidate[2] == 'Correy':
            vote_correy += 1

        elif candidate[2] == 'Li':
            vote_li += 1

        elif candidate[2] == "O'Tooley":
            vote_otooley += 1

    #This works below the counter but not above. Weird.
    total_votes = len(list(csvreader)


    # Calculate vote percentages
    # percent_khan = vote_khan / 3521001
    # percent_correy = vote_correy / total_votes
    # percent_li = vote_li / total_votes
    # percent_otooley = vote_otooley / total_votes 

    
    print('The vote count for Khan is ' + vote_khan)
    #print(vote_khan) 
    



    # print("The vote count for Correy is")
    # print(vote_correy)
    # print("The vote count for Li is") 
    # print(vote_li)
    # print("The vote count for O'Tooley is") 
    # print(vote_otooley)

