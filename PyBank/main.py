import os
import csv

# Create file name
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Declare lists
dates = []
profit_losses = []
profit_changes = []

# Read/load file into lists
with open(csvpath) as csvfile:
    # Drop header row
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        # Add dates
        dates.append(row[0])
        # Add profit/losses
        profit_losses.append(float(row[1]))

    # Add total
    total_months = len(dates)
    total_net = 0
    for profit_loss in profit_losses:
        total_net = total_net + profit_loss

    # Calculate changes
    current_value = 0
    previous_value = 0
    total_change = 0
    for i in range(1, len(profit_losses)):
        current_value = profit_losses[i]
        previous_value = profit_losses[i - 1]
        current_change = current_value - previous_value
        profit_changes.append(current_change)

    # Analyze data
    average_change = sum(profit_changes)/len(profit_changes)
    greatest_increase = max(profit_changes)
    high_index = profit_changes.index(greatest_increase)
    greatest_decrease = min(profit_changes)
    low_index = profit_changes.index(greatest_decrease)

    # Print results
    print("Financial Analysis")
    print("--------------------------------------")
    print(f"Total Months: {int(total_months)}")
    print(f"Total: ${int(total_net)}")
    print(f"Average Change: ${int(round(average_change))}")
    print(f"Greatest Increase in Profits: {dates[25]} ${int(greatest_increase)}")
    print(f"Greatest Decrease in Profits: {dates[44]} ${int(greatest_decrease)}")

# Write new file
f = open("PyBank.txt", "w")
f.write("Financial Analysis\n")
f.write("--------------------------------------\n")
f.write(f"Total Months: {int(total_months)} \n")
f.write(f"Total: ${int(total_net)}\n")
f.write(f"Average Change: ${int(round(average_change))} \n")
f.write(f"Greatest Increase in Profits: {dates[25]} ${int(greatest_increase)} \n")
f.write(f"Greatest Decrease in Profits: {dates[44]} ${int(greatest_decrease)} \n")
f.close()

