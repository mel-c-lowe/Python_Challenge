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
    #print(f"CSV Header: {header}")

    # Establish empty list for candidate column
    vote_cast = []

    # Loop through data to fill vote_cast list
    for voter in electionreader:

        vote_cast.append(str(voter[2]))
        
    # That's all I need in that loop because now I can read my list 
    # and set the csvfile aside as all additional data will not impact
    # the election results
    # Credit to Stephanie Richards for sharing her approach to pull data to a lists vs a dictionary
    # This helped me simplify a LOT of the work that had me stumped.

# Count the number of votes
total_vote_count = len(vote_cast)
#print(total_vote_count)

# Identify unique names in vote_cast list
# Count appearances of each name in vote_cast list

# Identify the unique candidates
unique_candidates = []

for vote in vote_cast:

        # Look through the list
        if vote not in unique_candidates:
            unique_candidates.append(vote)

# Check to see list has all 4 and only 4 desired candidates
print(unique_candidates)

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
# I have tried numerous formatting opetions, but it either gives me no zeros after the decimal
# or it gives me 6.  Since all the numbers round to a whole number (no value in the decimal place),
# I elected to be satisfied with this formatting.
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
election_winner = max(percent_of_vote)
index_for_winner = percent_of_vote.index(election_winner)
winner = unique_candidates[index_for_winner]
print(winner)


# Results Formatting
# Following the example of Stephanie Richards and Beau Jeffrey, I removed the hardcoding 
# of four lines, one for each candidate, and zipped my reference lists into a tuple.
# Many thanks to them for sharing their idea!
# And many thanks to TA Benji for heling me print the tuple to a text file!

election_results_tuple = tuple(zip(unique_candidates, percent_of_vote, candidate_votes))
print(election_results_tuple)

print("Election Results")
print("----------------------------------")
print(f"Total Votes:  {total_vote_count}")
print("----------------------------------")
for entry in election_results_tuple:
        print(f'{entry[0]}: {entry[1]} {entry[2]}')
print("----------------------------------")
print(f"Winner : {winner}")
print("----------------------------------")


# Thanks to Beau Jeffrey for cracking the \n new line syntax and sharing with me!
# I have not applied \n to all lines because of issues printing the tuple
# This combination simplified the instructions, but ensured appropriate printing of the tuple,
# so I decided to keep it as it is below.
analysis_textfile = os.path.join("Analysis", "PyPoll Analysis.txt")

with open(analysis_textfile, "w") as PyPoll_Analysis:

    print("Election Results\n"
    "----------------------------------\n"
    f"Total Votes:  {total_vote_count}\n"
    "----------------------------------", file = PyPoll_Analysis)
    for entry in election_results_tuple:
        print(f'{entry[0]}: {entry[1]} {entry[2]}', file = PyPoll_Analysis)
    print("----------------------------------\n"
    f"Winner : {winner}", file = PyPoll_Analysis)
