analysis_textfile = os.path.join("Analysis, "PyBank Analysis")

with open(analysis_textfile, "w") as PyBank_Analysis:

    file.write(
    print("Financial Analysis")
    print("----------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${sum_of_pl}")
    print(f"Average Change:  ${average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}")
    )
    file.close()