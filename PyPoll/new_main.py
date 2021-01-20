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

unique_candidates = []
otal_votes = 0

for vote in vote_cast:

        # Look through the list
        if vote not in unique_candidates:
            unique_candidates.append(vote)

# Check to see list has all 4 and only 4 desired candidates
print(unique_candidates)


# So, at this point, I have the vote total, 
# I've identified all the unique candidates
# But I have not counted how many votes went to each candidate
       


    
