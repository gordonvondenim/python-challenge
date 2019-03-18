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
    date= []
    header = next(reader)
   
    for row in reader:
        #total date & profit
        date.append(row[0]),
        profit_loss.append(float(row[1]))
    print("financial analysis:")
    print("-------------------------------------")
    print(f'Total date: {len(date)}')
    print(f'Total: ${sum(profit_loss)}')

    for i in range(1,len(profit_loss)):
    #min,max,avg chg
        profit_loss_change.append(profit_loss[i] - profit_loss[i-1])
        avg_profit_loss_change = sum(profit_loss_change) / len(profit_loss_change)
        max_profit_loss_change = max(profit_loss)
        min_profit_loss_change = min(profit_loss)

    #set dates
        max_profit_loss_change_date = str(date[profit_loss.index(max(profit_loss))])
        min_profit_loss_change_date = str(date[profit_loss.index(min(profit_loss))])
    
    #print results
    print(f' Average Change: $ {round(avg_profit_loss_change)}')
    print(f'Greatest Increase:', max_profit_loss_change_date, max_profit_loss_change)
    print(f'Greatest Decrease:', min_profit_loss_change_date, min_profit_loss_change)
    # increase/decrease still importing value of day that the variance occurred
    # cannot figure out code to import the value

    




