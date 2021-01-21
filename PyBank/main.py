# Import OS and CSV reader modules
import os
import csv

# Describe the file path to the CSV file
bank_csv = os.path.join('Resources', 'budget_data.csv')

# Make sure it's reading
with open(bank_csv) as bank_data:

    # Denote delimiter
    bankreader = csv.reader(bank_data, delimiter=',')
    csv_header = next(bankreader)
    print(csv_header)

    # What lists would help calculate net total?
    # List of months to later find index of greatest change
    # List of values in profit/loss to be able to do calculations with csv file closed
    net_total = 0
    month = []
    profit_loss = []

    for entry in bankreader:

        # Add to lists
        month.append(str(entry[0]))
        profit_loss.append(int(entry[1]))
        # print(month)
        # print(profit_loss)

# Calculate net_total

net_total = sum(profit_loss)
print(net_total)

# Calculate number of months
number_of_months = len(month)
print(number_of_months)

# Make a list of the changes between months
# This is a list of 85 changes (space between months)
# To be able to compare to other lists, it needs an additional row
# Better at the beginning or end?? Does it matter?




