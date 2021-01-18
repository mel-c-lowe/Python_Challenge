# Import OS and CSV reader modules
import os
import csv

# Describe file path to CSV file
#election_csv = os.path.join('Resources', 'election_data.csv')

# candidates = {}
#What I want to do is build a dictionary where the key is name
#and the values are the unique candidate names
#but I don't know how to do that

#Set up to read csv
with open(election_csv, 'r') as csvfile:

    #split by commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #Fake prompt to test that csvreader is working
    #ok, it's reading. now add a counter
    candidate = input("What candidate are you looking for?")

    #loop through data
    for row in csvreader:

        #tell it to check COLUMN 3 [2] for candidate names
        candidate = str(election_csv)
        
        list_of_candidate = list.count(candidate)

        if candidate == row[2]:
            print (candidate)









# Establish one function to calculate all election results
# with 'election_data' as the sole parameter
# def election_results(election_data):

#     # What elements do I need to work with?
#     candidate = unique name as appears in column [2]
#     total_votes = number of rows
#     candidate_vote_count = number of appearances of each name in column [2]
#     winner = candidate with highest candidate_vote_count









#Everything below here works, I'm just trying a new way to do some stuff

    # # Make sure that worked
    # # Great! At least the header is working
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # # This feels like a stupid and inelegant way to identify what the ouput number is
    # # But I'll fix it if I have time later in the week
    # vote_count = len(list(csvreader))
    # print("The total number of votes is")
    # print(vote_count)

   





    

