# modules
import os
import csv

# initialize variables
months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

# Path to Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(csvpath) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # header row first
    csv_header = next(csvfile)
             
    # Read through each row of data after the header
    for row in csv_reader:

        # Count of months
        count_months += 1

        # Net total amount of "Profit/Losses" 
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append months
            months.append(row[0])

            # Append profit_loss_changes
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    #sum and average of the changes in "Profit/Losses"
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    # highest and lowest changes in "Profit/Losses"
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # highest and lowest changes in "Profit/Losses"
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# Print the financial analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


# Export a text file with the results
analysis_file = os.path.join("Analysis", "budget_data.txt")
with open(analysis_file, "w") as txtfile:

    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months:  {count_months}\n")
    txtfile.write(f"Total:  ${net_profit_loss}\n")
    txtfile.write(f"Average Change:  ${average_profit_loss}\n")
    txtfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    txtfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")