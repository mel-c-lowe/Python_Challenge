# Import OS and CSV modules
import os 
import csv 

# Establish file path
election_csv_file = os.path.join("Resources", "election_data.csv")

# Set up to read election_csv_file and refer to it as election_data
with open(election_csv_file) as election_data:

    # Build the csvreader, print header to confirm document is reading
    electionreader = csv.reader(election_data, delimiter=",")
    header = next(electionreader)
    print(f"CSV Header: {header}")

    # Establish empty list for candidate column
    vote_cast = []

    # Loop through data to fill vote_cast list
    for voter in electionreader:

        vote_cast.append(str(voter[2]))
        
    # That's all I need in that loop because now I can read my list 
    # and set the csvfile aside as all additional data will not impact
    # the election results

# Count the number of votes
vote_count = len(vote_cast)
print(vote_count)

# Identify unique names in vote_cast list
# Count appearances of each name in vote_cast list

# This stuff is different 

# Identify the unique candidates
unique_candidates = []

for vote in vote_cast:

        # Look through the list
        if vote not in unique_candidates:
            unique_candidates.append(vote)

# Check to see list has all 4 and only 4 desired candidates
print(unique_candidates)


# So, at this point, I have the vote total, 
# I've identified all the unique candidates
# But I have not counted how many votes went to each candidate

# Identify vote counts for each candidate
candidate_votes = []

# Start with the list of all votes cast and counter of 0
vote_count = 0
for vote in unique_candidates:
    # And compare to name in candidate list
    for name in vote_cast:
        # Start running total of votes for candidates
        if vote == name:
            vote_count = int(vote_count) + 1

    # Add to the list
    candidate_votes.append(vote_count)

    #Reset counter for next unique name
    vote_count = 0
  
print(candidate_votes)


# Identify winner
# election_winner = max(candidate_votes)
# print(election_winner)





       


    
