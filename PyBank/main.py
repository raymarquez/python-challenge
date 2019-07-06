import os   
import csv    
PyBank_csv = os.path.join("budget_data.csv")

x = 0
pnlChange = []
pnlAmount = []
pnlPeriod = []
pnlNet = 0
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
        if x == 1: periodBeg = pnlPeriod[x-1]                                   #-- capture latest date in period
        else: periodEnd = pnlPeriod[x-1]                                        #-- capture earliest date in period
                    
for s in range (x):        
    pnlNet += int(float(pnlAmount[s]))                                          #-- aggregate Net PnL
    if s < x-1: pnlAvg += float(pnlChange[s])                                   #-- aggregate Changes for averaging later
    if pnlMax < pnlChange[s-1]: 
        pnlMax = pnlChange[s-1]                                                 #-- capture max change and date
        periodMax = pnlPeriod[s]
    if pnlMin > pnlChange[s-1]: 
        pnlMin = pnlChange[s-1]                                                 #-- capture min change and date
        periodMin = pnlPeriod[s]
    
pnlAvg = round((pnlAvg / len(pnlChange)) ,2)                                    #-- Average Net Changes, rounded to 2 decimals
    
print ('----------------------------------------------------------------')
print (f'  Financial Analysis:                 from {periodBeg} to {periodEnd}')
print ('----------------------------------------------------------------')
print (f'   Total Periods (months)                       :  {x}') 
print (f'   Total Net Amount (PnL)                       :  ${pnlNet}')
print (f'   Average Change                               :  ${pnlAvg}')
print (f'   Greatest Increase in Profits was on {periodMax} :  ${pnlMax}')
print (f'   Greatest Decrease in Profits was on {periodMin} :  ${pnlMin}')
print ('----------------------------------------------------------------')


WinHdg = []
#WinDtl = []
#WinDtl2 = []
#WinHdgTotal = "Financial Analyis :"
#WinHdgCandidates = "Number of Candidates :"
#WinHdgChamp = "CONGRATULATIONS!The winner is  :"
hdg00 = "Financial Analysis:                     from " + str(periodBeg) + "   to " + str(periodEnd)
hdg01 = "Total Periods (months)   : $" + str(x)
hdg02 = "Total Net Amount (PnL)  : $" + str(pnlNet)
hdg03 = "Average Change               : $" + str(pnlAvg)
hdg04 = "Greatest Increase in Profits was on " + str(periodMax) + "  : $" + str(pnlMax)
hdg05 = "Greatest Decrease in Profits was on " + str(periodMin) + " :  $" + str(pnlMin)


WinHdg =[(hdg00),(hdg01),(hdg02),(hdg03),(hdg04),(hdg05)]
#WinDtl =[i,len(fndCandidate),"",winnerName]
winners = zip(WinHdg)

winner_out = os.path.join("mywinner_out.csv")
with open (winner_out,"w",newline="") as winner_file:
    writer=csv.writer(winner_file)
    writer.writerows(winners)
