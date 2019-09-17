import csv
import os 

budget_data = os.path.join("..", "python-challenge","PyBank", "budget_data.csv") 
Analysis = os.path.join ("..", "python-challenge","PyBank","budget_analysis.txt") 
total_months = 0
total_pl = 0
checker = 0
change = 0
dates = []
pnl = []

with open (budget_data, newline = "") as csvfile:
     csvreader = csv.reader(csvfile,delimiter = ",")
     cvs_header = next(csvreader)
     #print(f"cvs_header:{cvs_header}")
     
     first_row = next(csvreader)
     #print(first_row)
     total_months +=1
     #print(total_months)
     total_pl += int(first_row[1])
     checker = int(first_row[1])
     #print(total_pl)
     #print(checker)
     for row in csvreader:
         dates.append(row[0])
         change = int(row[1])-checker
         pnl.append(change)
         checker = int(row[1])
         total_months += 1
         total_pl = total_pl + int(row[1])
         #print(total_months)

greatest_increase = max(pnl)
greatest_index = pnl.index(greatest_increase)
greatest_date = dates[greatest_index]

greatest_decrease = min(pnl)
low_index = pnl.index(greatest_decrease)
low_date = dates[low_index]

avg_change = sum(pnl)/ len(pnl)
#print(greatest_decrease)
#print(greatest_increase)
#print(greatest_date)  
#print(greatest_index)       
#print (pnl)
#print(len(pnl))
#print(len(dates))
#print(avg_change)

report = (
f"Total Months: {total_months} \n"
f"Total Revenue: {total_pl}\n"
f"Average Revenue Change: $ {avg_change}\n"
f"Greatest Increase in Profits and Loses: {greatest_date} ${greatest_increase}\n"
f"Greatest Decrease in Profits and Loses : {low_date} ${greatest_decrease}\n")

with open(Analysis, "w") as txt_file:
    txt_file.write(report)






