import os
import csv
PyPoll_csv = os.path.join("election_data.csv")

inVoterID = []
inCounty = []
inCandidate = []
fndCandidate = []
fndCount = []
k = 0
i = 0
sample = 100
f = 0
pct = 0.00
winnerName = ""
winnerPct = 0.0

WinHdg = []
WinDtl = []
WinDtl2 = []
WinHdgTotal = "Total Number of Votes Cast :"
WinHdgCandidates = "Number of Candidates :"
WinHdgChamp = "CONGRATULATIONS!The winner is  :"

WinHdgVotesTitle = "Votes for :"
WinHdgVotesName = ["","Candidate","=========="]
WinDtlVotesPct = ["","Percent Vote","=========="]
WinDtlVotesCount = ["","Number of Votes ","=========="]
#>>WinntlName = ""
#>>WinDtlPct = 0
#>>WinDtlVotesEach = 0
#>>WinDtlTotal = 0
#>>WinDtlCandidates = 0
#>>WinDtlChamp = ""

with open (PyPoll_csv,newline="") as PyPoll_file:
    PyPoll_row = csv.reader(PyPoll_file,delimiter=',')
    PyPoll_hdr = next(PyPoll_row)
    
    for row in PyPoll_row:
        #>>if i < sample:
        inVoterID.append(row[0])                                        #-- get Voter ID
        inCounty.append(row[1])                                         #-- get County
        inCandidate.append(row[2])                                      #-- get Candidate
        #>>else: break
                
        if inCandidate[i] in fndCandidate:
            fndCount = fndCandidate.index(inCandidate[i])
        else:
            fndCandidate.append(row[2])  
            f += 1
        
        i += 1                                                              #-- get next

print (f' ===================================================================')
print (f'            Total Number of Votes Cast : {i}')
print (f'                  Number of Candidates : {len(fndCandidate)}')
print (f' -------------------------------------------------------------------')
print (f'            Votes for                  :')

for fnd in range(len(fndCandidate)):
    k = inCandidate.count(fndCandidate[fnd])
    pct = round((k/(i)*100),0)
    print (f'            ----- {fndCandidate[fnd]} -----  {pct} percent ( total votes: {k} )')
    WinHdgVotesName.append(fndCandidate[fnd])
    WinDtlVotesPct.append(pct)
    WinDtlVotesCount.append(k)
    if pct > winnerPct:
        winnerPct = pct
        winnerName = fndCandidate[fnd]

print (f' -------------------------------------------------------------------')
print (f'            CONGRATULATIONS!   The winner is {winnerName}  !!! ')
print (f'            CONGRATULATIONS!   The winner is {winnerName}  !!! ')
print (f'            CONGRATULATIONS!   The winner is {winnerName}  !!! ')
print (f' ===================================================================')

WinHdg =[(WinHdgTotal),(WinHdgCandidates),(WinHdgVotesTitle),(WinHdgChamp)]
WinDtl =[i,len(fndCandidate),"",winnerName]

winners = zip(WinHdg,WinDtl)

winner_out = os.path.join("mywinner_out.csv")
with open (winner_out,"w",newline="") as winner_file:
    writer=csv.writer(winner_file)
    writer.writerows(winners)
    
    winners = zip(WinHdgVotesName,WinDtlVotesPct,WinDtlVotesCount)
    writer.writerows(winners)

results = zip(inCandidate,inCounty,inVoterID)
results_out = os.path.join("myresults_out.csv")
with open (results_out,"w",newline="") as results_file:
    writer=csv.writer(results_file)
    writer.writerow(["Candidate","County","VoterID"])
    writer.writerows(results)
