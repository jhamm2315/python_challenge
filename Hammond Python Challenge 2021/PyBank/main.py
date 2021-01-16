#Create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

import os
import csv

#Set variables
MonthCount = 0
Total = 0
PL = []
monthList = []
monthlyChanges = []

#Pull in data & read file
csvpath = os.path.join("Resources","budget_data.csv")
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader)
    
    for row in csv_reader:
        MonthCount += 1
        Total += int(row[1])
        PL.append(row[1])
        monthList.append(row[0])

#First month P&L value
firstPL = int(PL[0])

#This loop creates a list of monthly changes
for i in range(1, len(PL)):
    monthlyChanges.append(int(PL[i]) - firstPL)
    firstPL = int(PL[i])
    i += 1

AvgChange = sum(monthlyChanges) / len(monthlyChanges)

#Find max increase and min increase
MaxIncrease = max(monthlyChanges)
MaxDecrease = min(monthlyChanges)

#Find month index for the Max Increase and Max Decrease
for i in range(len(monthlyChanges)):
    if monthlyChanges[i] == MaxIncrease:
        maxIndex = (i - 1)
    elif monthlyChanges[i] == MaxDecrease:
        minIndex = (i - 1)
    else:
        i += 1
        
MaxMonth = monthList[maxIndex]
MinMonth = monthList[minIndex]

#Print results           
print()
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {MonthCount}")
print(f"Total: ${Total}")
print(f"Average Change: ${AvgChange}")
print(f"Greatest Increase in Profits: {MaxMonth}  (${MaxIncrease})")
print(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")
 

 #open a file for writing:
f = open("Resources" , "analysis.txt")
print("Financial Analysis",file=f)
print("--------------------------------", file=f)
print(f"Total Months: {MonthCount}",file=f)
print(f"Total: ${Total}", file=f)
print(f"Average Change: ${AvgChange}",file=f)
print(f"Greatest Increase in Profits: {MaxMonth}  (${MaxIncrease})",file=f)
print(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})",file=f)


f.close()

#Financial Analysis
#--------------------------------
#Total Months: 86
#Total: $38382578
#Average Change: $-2315.1176470588234
#Greatest Increase in Profits: Dec-11  ($1926159)
#Greatest Decrease in Profits: Jul-13 ($-2196167)