import csv
import os

budget_data = os.path.join('/Users/Sam/Desktop/MY_UC_BERK/CHALLENGES/CHALLENGE_3/Starter_Code/PyBank/Resources/budget_data.csv')
months = 0
profit = 0
profit_changes = []


with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skips header row
    header = next(csvreader)
    rows = list(csvreader)

    #Initiates previous row
    previous_profit = int(rows[0][1])

    
    for row in rows:
        # Counts number of months
        months += 1
        # Gets total amount of profit/losses
        profit += int(row[1])
        # Calculate change in profit/losses
        profit_change = int(row[1]) - previous_profit

        # Adds changes to list
        profit_changes.append(profit_change)
     
        # Sets previous profit back to current profit
        previous_profit = int(row[1])
    
        
# Calculates average change in profit/losses
average_change = sum(profit_changes) / len(profit_changes)

# Calculates greatest increase in profit and date
greatest_increase = max(profit_changes)
greatest_increase_date = str(rows[profit_changes.index(greatest_increase)][0])

# Calculates greatest decrease in profit and date
greatest_decrease = min(profit_changes)
greatest_decrease_date = str(rows[profit_changes.index(greatest_decrease)][0])

# Prints results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${profit}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")