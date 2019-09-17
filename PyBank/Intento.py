import csv
import os 

csvfile = os.path.join("..", "python-challenge","PyBank", "budget_data.csv")  

total_months = []
total_profit = []
average_change = []


with open (csvfile, newline = "") as csvfile:
     csvreader = csv.reader(csvfile,delimiter = ",")
     header = next(csvreader)
     print(f"header:{header}")
     for row in csvreader:
         total_months.append(row[0])
         total_profit.append(int(row[1]))
     for x in range(1, len(total_profit)):
        average_change.append((int(total_profit[x]) - int(total_profit[x-1])))
     average_change= sum(average_change)/ len(average_change)
    
     
     max_increase_value = max (str(average_change))
     max_decrease_value = min (str(average_change))

     max_increase_month = str (average_change).index(max (str(average_change))) +1
     max_decrease_month = str (average_change).index(min (str(average_change))) +1





print("Reporte Financiero") 
print(f"Total Meses: {len(total_months)}")
print(f"Total ganacias: {sum(total_profit)}")
print("Total Cambio:" + str(average_change))
print(f"Mayor Incremento Ganancias: {total_months[max_increase_month]} (${(max_increase_value)})")
print(f"Mayor Decrecimiento Ganancias {total_months[max_decrease_month]} (${(max_decrease_value)})")

report = f""
file_report = open("PyBankReport.txt" , "w")
file_report.write(report)
file_report.close()

print(report)
















