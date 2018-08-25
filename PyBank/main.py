import os
import csv

budgetdatacsv = os.path.join('Resources', 'budget_data.csv')

def read_budget_csv(inputcsv):
    totalmonths = 1
    totalamount = 0
    changedict = {}

    with open(inputcsv, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvfile, None)
        previous_row = next(csvreader)
        totalamount = int(previous_row[1])

        for row in csvreader:
            totalmonths += 1
            current_row = row
            totalamount += int(current_row[1])
            changedict[current_row[0]] = int(current_row[1]) - int(previous_row[1])
            previous_row = current_row
        
        avgchange = sum(changedict.values())*1.0/(totalmonths-1)
        maxprofit = max(changedict.values())
        minloss = min(changedict.values())
        maxmonth = max(changedict, key=changedict.get)
        minmonth = min(changedict, key=changedict.get)

        output = {
        "Total Months:" : totalmonths,
        "Total:": "$"+str(totalamount),
        "Average  Change:" : "$"+str(round(avgchange,2)),
        "Greatest Increase in Profits:" : maxmonth + " ($" + str(maxprofit) + ")",
        "Greatest Decrease in Profits:" : minmonth + " ($" + str(minloss) + ")"
        }
    
    return output

def print_dict(dictoutput):
    for key,value in dictoutput.items():
        print(key, value)

def write_output_csv(outputcsv):
    with open(outputcsv, 'w') as outputfile:
        outputfile.write("Financial Analysis" + os.linesep)
        outputfile.write("--------------------------------"+ os.linesep)
        for key,value in dictout.items():
            outputfile.write(str(key) +" " + str(value)+ os.linesep)



outputcsv = "output_budget.txt"
print('Financial Analysis')
print("--------------------------------")
dictout = read_budget_csv(budgetdatacsv)
print_dict(dictout)
write_output_csv(outputcsv)