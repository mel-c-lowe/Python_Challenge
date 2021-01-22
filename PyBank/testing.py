# Import OS and CSV reader modules
import os
import csv

# Describe the file path to the CSV file
bank_csv = os.path.join('Resources', 'budget_data.csv')

# Make sure it's reading
with open(bank_csv, 'r') as bank_data:

    # Denote delimiter
    # next(csvreader) means read and return current row THEN move to next row
    # Kelly Devillier helped me set this up
    csvreader = csv.reader(bank_data, delimiter=',')
    csv_header = next(csvreader) # save the header in csv_header, move to next row
    print(csv_header) 
    print("----------------------------------")
    previous_row = next(csvreader) # save data in row two for Jan-2010 in previous_row, move to next row

    # Define lists to create while reading the csv
    # Be sure to addend data stored in previous_row to start the list when needed

    changes_between_months = []
    list_of_months = []
    list_of_months.append(previous_row[0])
    list_of_profitloss = []
    list_of_profitloss.append(previous_row[1])
    previous_profitloss = int(previous_row[1])
    sum_of_pl = previous_profitloss
   
    print(f"Starting number for Total PL:  {previous_profitloss}")
    print("----------------------------------")

    for row in csvreader:

        # print(row)
        # print(previous_row)
        change = int(row[1]) - int(previous_row[1])
        changes_between_months.append(change)

        month = str(row[0])
        list_of_months.append(month)

        profitloss_value = int(row[1])
        # list_of_profitloss.append(profitloss_value)
        sum_of_pl = sum_of_pl + profitloss_value

        previous_row = row

# Calculate total profit/loss
print(sum_of_pl)