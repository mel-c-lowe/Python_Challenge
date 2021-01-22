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
total_vote_count = len(vote_cast)
print(total_vote_count)

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

# Calculate percentages, use float to keep numbers after decimal
# Round to three decimal places
# 
percent_of_vote = []
for each in (candidate_votes):
    vote_percent = round(float(int(each) / int(total_vote_count)), 3)
    percentage = "{:.00%}".format(vote_percent)
    percent_of_vote.append(percentage)

# print(percentage)


# Ok, so I now have three lists: candidate names, vote counts, and percentages
# The first determines the order in which the second two display data as it is used
# as the initial comparison to draw out the counts and calculate percentages

# Identify winner
# This is only pulling the winning percent of vote. Grrr.
election_winner = max(percent_of_vote)
index_for_winner = percent_of_vote.index(election_winner)
winner = unique_candidates[index_for_winner]
print(winner)


# Results Formatting
# I recognize that this is hardcoding that makes the results print out not compatible to 
# CSV files with less or more than 4 candidates. My intention was to resolve that,
# but I ran out of time.

print("Election Results")
print("----------------------------------")
print(f"Total Votes:  {total_vote_count}")
print("----------------------------------")
print(f'{unique_candidates[0]}: {(percent_of_vote[0])} ({(candidate_votes[0])})')
print(f'{unique_candidates[1]}: {(percent_of_vote[1])} ({(candidate_votes[1])})')
print(f'{unique_candidates[2]}: {(percent_of_vote[2])} ({(candidate_votes[2])})')
print(f'{unique_candidates[3]}: {(percent_of_vote[3])} ({(candidate_votes[3])})')
print("----------------------------------")
print(f"Winner : {winner}")
print("----------------------------------")

# Attempt 1 at writing a txt file
analysis_textfile = os.path.join("Analysis", "PyPoll Analysis.txt")

with open(analysis_textfile, "w") as PyPoll_Analysis:

    print("Election Results", file = PyPoll_Analysis)
    print("----------------------------------", file = PyPoll_Analysis)
    print(f"Total Votes:  {total_vote_count}", file = PyPoll_Analysis)
    print("----------------------------------", file = PyPoll_Analysis)
    print(f'{unique_candidates[0]}: {(percent_of_vote[0])} ({(candidate_votes[0])})', file = PyPoll_Analysis)
    print(f'{unique_candidates[1]}: {(percent_of_vote[1])} ({(candidate_votes[1])})', file = PyPoll_Analysis)
    print(f'{unique_candidates[2]}: {(percent_of_vote[2])} ({(candidate_votes[2])})', file = PyPoll_Analysis)
    print(f'{unique_candidates[3]}: {(percent_of_vote[3])} ({(candidate_votes[3])})', file = PyPoll_Analysis)
    print("----------------------------------", file = PyPoll_Analysis)
    print(f"Winner : {winner}", file = PyPoll_Analysis)
    print("----------------------------------", file = PyPoll_Analysis)

       


    
