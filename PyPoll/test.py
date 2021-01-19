# Import OS and CSV reader modules
import os
import csv

# Describe file path to CSV file
election_csv = os.path.join('Resources', 'election_data.csv')

# Blank list to collect candidate names in column [2]
candidate_list []

#Set up to read csv
with open(election_csv, 'r') as election_data:

    #split by commas
    csvreader = csv.reader(election_data, delimiter=',')
    csv_header = next(csvreader)
    
    for candidate in csvreader:
        if candidate[2] == #first occurence:
            candidate_list.append(candidate)
    print(candidate_list)


# could I do a while loop starting with an empty variable 'active_candidate'?
    # candidate = []
    #while candidate == "this is where I don't know how to execute"
        #put active candidate into dictionary as a value to key of Candidate
        #if candidate == the next row, then
            #add to the counter for that candidate
            #append candidate name to list of candidates?
            #use list to create dictionary
                #maybe no?
            #produce results based on dictionary???