# Import OS and CSV reader modules
import os
import csv

# Describe the file path to the CSV file
bank_csv = os.path.join('Resources', 'budget_data.csv')

# Make sure it's reading
with open(bank_csv, 'r') as bank_data:

    # Denote delimiter
    # next(csvreader) means read and return current row THEN move to next row
    # Kelly Devillier helped me set this up, thanks Kelly!
    csvreader = csv.reader(bank_data, delimiter=',')
    csv_header = next(csvreader) # save the header in csv_header, move to next row
    # print(csv_header) 
    previous_row = next(csvreader) # save data in row two for Jan-2010 in previous_row, move to next row

    # Define lists to create while reading the csv
    # Be sure to append data stored in previous_row to start the list when needed

    changes_between_months = []
    # Add a zero to beginning to change list to align number of entries
    changes_between_months.append(0)
    list_of_months = []
    list_of_months.append(previous_row[0])
    list_of_profitloss = []
    list_of_profitloss.append(previous_row[1])
    previous_profitloss = int(previous_row[1])
    sum_of_pl = previous_profitloss
   
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

# Calculate Total Months
total_months = len(list_of_months)
# print(total_months)

# Total of profit/loss calculated in for-loop
# print(sum_of_pl)

# Calculate Average Change
total_changes = sum(changes_between_months)
# print(total_changes)
average_change = round(total_changes / (len(changes_between_months) - 1), 2)
# print(average_change)

# Calculate Greatest Increase
# Find month of greatest increase
# Thanks to Stephanie Richards for modeling the comparison of index locations!
# I knew I wanted to do this and seeing her approach helped me actually execute on it.
greatest_increase = max(changes_between_months)
index_for_increase = changes_between_months.index(greatest_increase)
greatest_increase_month = list_of_months[index_for_increase]
# print(greatest_increase_month)


# Calculate Greatest Decrease
# Find month of greatest decrease
greatest_decrease = min(changes_between_months)
index_for_decrease = changes_between_months.index(greatest_decrease)
greatest_decrease_month = list_of_months[index_for_decrease]
# print(greatest_decrease_month)

# Results Formatting

print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${sum_of_pl}")
print(f"Average Change:  ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}")


# Attempt 1 at writing a txt file was long and had file = PyBank_Analysis after every line
# Attempt 2 credit must go to Beau Jeffrey, who shared a more concise new line syntax
# that makes the whole thing look a lot cleaner. Thanks, Beau!
analysis_textfile = os.path.join("Analysis", "PyBank Analysis.txt")

with open(analysis_textfile, "w") as PyBank_Analysis:

    print("Financial Analysis\n"
    "----------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${sum_of_pl}\n"
    f"Average Change:  ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}", file = PyBank_Analysis)



        
   
