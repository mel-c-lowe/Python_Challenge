# Import OS and CSV reader modules
import os
import csv

# Describe the file path to the CSV file
bank_csv = os.path.join('Resources', 'budget_data.csv')

profit_loss_start = 0
profit_loss_end = 0

# Make sure it's reading
with open(bank_csv, 'r') as bank_data:

# Denote delimiter
    csvreader = csv.reader(bank_data, delimiter=',')
    csv_header = next(csvreader)


  #beau is the best



    for row in csvreader:

        month_count = str(row[0])
        

        total_months = len(list(csvreader)) - 1

        if total_months == 1:
            first_row = profit_loss_start

        else:
            last_row = profit_loss_end

        print(profit_loss_start)
        print(profit_loss_end)