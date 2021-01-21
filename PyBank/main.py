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

        # If I pick up each entry and treat it as monthly_value, 
        # I can add each new monthly value through the loop to net_total

        # monthly_value = int(entry[1])
        # net_total = net_total + monthly_value
        # print(net_total)
        # That didn't work

net_total = sum(profit_loss)
print(net_total)


