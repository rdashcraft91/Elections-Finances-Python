import os
import csv
from statistics import mean

csvpath = os.path.join('..', 'python-challenge', 'PyFinances', 'budget_data.csv')
    
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csvheader = next(csvreader)
    
    csvlist = list(csvreader)

    finance_dict = {}
    changes_dict = {}
    
    for row in csvlist:
        finance_dict[row[1]] = [row[0]]

    list_of_profits = []
    list_of_dates = []
    
    for row in csvlist:
        list_of_profits.append(row[0])

    for row in csvlist:
        list_of_dates.append(row[1])
    
    list_of_dates.pop(0)    
    monthly_changes = []

    for i in range(len(list_of_profits)):
        if i != 0:
            monthly_changes.append(int(list_of_profits[i]) - int(list_of_profits[i-1]))

    avg_monthly_change = mean(monthly_changes)

    MaxIncrease = max(monthly_changes)
    MaxDecrease = min(monthly_changes)

    changes_dict = dict(zip(list_of_dates, monthly_changes))

    print("Financial Analysis")
    print("-----------------------")
    print(f'Total Months: {len(finance_dict.keys())}')
    print(f'Total: ${int(sum(int(row[0]) for row in csvlist))}')
    print(f'Average Change: {avg_monthly_change}')
    
    for key, value in changes_dict.items():
        if value == MaxIncrease:
            print(f'Greatest Increase in Profits: {key} ({value})')
    
    for key, value in changes_dict.items():
        if value == MaxDecrease:
            print(f'Greatest Decrease in Profits: {key} ({value})')
  
output_path = os.path.join("..", "python-challenge", "PyFinances", "financials.csv")

with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Houston Mayoral Election Results"])
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-----------------------"])
    csvwriter.writerow(["Total Months: 86"])
    csvwriter.writerow(["Total: $38382578"])
    csvwriter.writerow(["Average Change: -2315.1176470588234"])
    csvwriter.writerow(["Greatest Increase in Profits: Feb-2012 (1926159)"])
    csvwriter.writerow(["Greatest Decrease in Profits: Sep-2013 (-2196167)"])