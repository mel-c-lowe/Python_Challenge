# Import OS and CSV reader modules
import os
import csv

# Describe the file path to the CSV file
bank_csv = os.path.join('Resources', 'budget_data.csv')

# Make sure it's reading
with open(bank_csv, 'r') as bank_data:

    # # Lets just lay out what I will need to work with
    # net_total = #sum of column[1]
    # total_months = len(list(csvreader))
    # change_over_period = #list of row+1 minus row, next row
    # avg_changes = #sum of all entries in change_over_period divided by len(list(csvreader))-1
    # greatest_increase = #iterate through change_over_period list and compare 
    #                     #row and row+1, keeping the greater and continung to iterate and use 
    #                     #the greater to compare the next row
    # greatest_decrease = #same as increase, but keep lesser value

    # Denote delimiter
    csvreader = csv.reader(bank_data, delimiter=',')
    csv_header = next(csvreader)

    # Total number of months
    # This feels inelegant, but better than main.py in pypoll, so we'll go with it
    # total_months = len(list(csvreader))
    # tm_lead = "Total Months:  "
    # print(tm_lead, total_months)


    #beau is the best

    for row in csvreader:

        month_count = str(row[0])
        profit_loss_start = int(row[1])
        profit_loss_end = int(row[1])

        total_months = len(list(csvreader)) - 1

        if total_months == 1:
            first_row = profit_loss_start

        else:
            last_row = profit_loss_end

        print(profit_loss_start)
        print(profit_loss_end)
        


   
