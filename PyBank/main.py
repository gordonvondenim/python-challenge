import os
import csv
import statistics

#choose where to read
budget_csv = os.path.join('..','budget.csv')
#check if file exists
#os.path.exists('budget.csv') test returned true

#read csv and print data
with open(budget_csv, newline='') as budget:
    reader = csv.reader(budget, delimiter = ",")
    #store as lists
    profit_loss = []
    profit_loss_change = []
    date = []
    header = next(reader)
   
    for row in reader:
        date.append(row[0]),
        profit_loss.append(float(row[1]))
    print("financial analysis:")
    print("-------------------------------------")
    print(f'Total Months: {len(date)}')
    print(f'Total: ${sum(profit_loss)}')
    print(f'Average Change: {statistics.mean(profit_loss)}')

    




