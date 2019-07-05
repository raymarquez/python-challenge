import os   
import csv      
PyBank_csv = os.path.join("budget_data.csv")

x = 0
pnlChange = []
pnlAmount = []
pnlPeriod = []
pnlNet = 0.0
pnlAvg = 0.0
pnlMax = 0.0
pnlMin = 0.0

with open(PyBank_csv,newline="") as PyBank_file: 
    PyBank_row = csv.reader(PyBank_file,delimiter=',')
    PyBank_hdr = next(PyBank_row)
    
    for row in PyBank_row:
        x += 1                                                                  #-- count data rows
        pnlAmount.append(row[1])                                                #-- collect pnl amounts
        pnlPeriod.append(row[0])                                                #-- collect periods
        if x > 1: pnlChange.append(int(pnlAmount [x-1]) - int(pnlAmount [x-2])) #-- calculate changes
        if x == 1: periodMin = pnlPeriod[x-1]                                   #-- capture latest date in period
        else: periodMax = pnlPeriod[x-1]                                        #-- capture earliest date in period
                    
for s in range (x):        
    pnlNet += int(float(pnlAmount[s]))                                          #-- aggregate Net PnL
    if s < x-1: pnlAvg += float(pnlChange[s])                                   #-- aggregate Changes for averaging later
    if pnlMax < pnlChange[s-1]: pnlMax = pnlChange[s-1]                         #-- capture max change
    if pnlMin > pnlChange[s-1]: pnlMin = pnlChange[s-1]                         #-- capture min change
    
pnlAvg = round((pnlAvg / len(pnlChange)) ,2)                                    #-- Average Net Changes, rounded to 2 decimals
    
print ('---------------------------------------------------------')
print (f'  Financial Analysis:      from {periodMin} to {periodMax}')
print ('---------------------------------------------------------')
print (f'   Total Months                 :  {x}') 
print (f'   Net Amount (PnL)             :  {pnlNet}')
print (f'   Average Change               : {pnlAvg}')
print (f'   Greatest Increase in Profits :  {pnlMax}')
print (f'   Greatest Decrease in Profits : {pnlMin}')
print ('---------------------------------------------------------')