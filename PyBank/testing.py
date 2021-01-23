# Attempt 1 at writing a txt file wrote the document line by line
# Thanks to Beau Jeffrey for cracking the \n new line syntax and sharing with me!
analysis_textfile = os.path.join("Analysis", "PyPoll Analysis.txt")

with open(analysis_textfile, "w") as PyPoll_Analysis:

    print("Election Results", file = PyPoll_Analysis)
    print("----------------------------------", file = PyPoll_Analysis)
    print(f"Total Votes:  {total_vote_count}", file = PyPoll_Analysis)
    print("----------------------------------", file = PyPoll_Analysis)
    for entry in election_results_tuple:
        print(f'{entry[0]}: {entry[1]} {entry[2]}', file = PyPoll_Analysis)
    print("----------------------------------", file = PyPoll_Analysis)
    print(f"Winner : {winner}", file = PyPoll_Analysis)





    # Attempt 1 at writing a txt file wrote the document line by line
# Thanks to Beau Jeffrey for cracking the \n new line syntax and sharing with me!
analysis_textfile = os.path.join("Analysis", "PyPoll Analysis.txt")

with open(analysis_textfile, "w") as PyPoll_Analysis:

    print("Election Results\n"
    print("----------------------------------\n"
    print(f"Total Votes:  {total_vote_count}\n"
    print("----------------------------------", file = PyPoll_Analysis)
    for entry in election_results_tuple:
        print(f'{entry[0]}: {entry[1]} {entry[2]}', file = PyPoll_Analysis)
    print("----------------------------------\n"
    print(f"Winner : {winner}", file = PyPoll_Analysis)