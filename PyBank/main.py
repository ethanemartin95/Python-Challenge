import os
import csv

#find file
csvdir = os.chdir('/Users/ethan_martin95/Documents/Georgia-Tech-Bootcamp-PULL/GT-ATL-DATA-PT-12-2019-U-C/Homework/03-Python/Instructions/PyBank/Resources')
csvpath_r = os.path.join('budget_data.csv')

#read in file AND create a Header
with open(csvpath_r, newline='') as csvfile_r:
    csvreader = csv.reader(csvfile_r, delimiter=',')
    csvheader = next(csvreader)

#intialize valiables and lists
    month_counter = 0
    profit_loss_total = 0
    months_of_change = 0

    date_list = []
    amount_change = []

#itialize variable to skip first row of data
    last_value = "First"

#iterate through entire CSV
    for row in csvreader:

#for each row, tally the dates
        month_counter += 1

#grab value of current row for later comparison
        current_value = row[1]

#ignore first row because there was no change
        if last_value is not "First":
#start calculating changes and add it to a list
            amount_change.append(int(current_value) - int(last_value))
#grab date of change
            date_list.append(row[0])
#start tallying the number of months we see change
            months_of_change += 1
#start storing values from previous row
        last_value = current_value
#total all profits and losses for each date
        profit_loss_total = profit_loss_total + int(row[1])

#initialize variables and lists
    change_total = 0
    greatest_inc_amount = amount_change[0]
    greatest_dec_amount = amount_change[0]

#get index values that will allow us to loop through amount_change and date_list
    for element in range(len(date_list)):
#total the changes for average calculation
        change_total = change_total + amount_change[element]

#Find greatest increase and decrease values and their dates
        if amount_change[element] > greatest_inc_amount:
            greatest_inc_amount = amount_change[element]
            greatest_inc_date = date_list[element]
        if amount_change[element] < greatest_dec_amount:
            greatest_dec_amount = amount_change[element]
            greatest_dec_date = date_list[element]

#print results to terminal
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {month_counter}')
    print(f'Total: ${profit_loss_total}')
    print(f'Average Change: ${round(change_total/months_of_change,2)}')
    print(f'Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc_amount})')
    print(f'Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec_amount})')

#create new text file to store results
    textdir = os.chdir('/Users/ethan_martin95/Documents/Georgia-Tech-Bootcamp-PUSH/Python-Challenge/PyBank')
    textpath_w = os.path.join('Py_Bank_Output.txt')

#store results in new text file
    with open(textpath_w, 'w') as textfile_w:
        textfile_w.write('Financial Analysis\n')
        textfile_w.write('----------------------------\n')
        textfile_w.write(f'Total Months: {month_counter}\n')
        textfile_w.write(f'Total: ${profit_loss_total}\n')
        textfile_w.write(f'Average Change: ${round(change_total/months_of_change,2)}\n')
        textfile_w.write(f'Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc_amount})\n')
        textfile_w.write(f'Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec_amount})\n')
