import csv
import os

election_data = os.path.join('/Users/Sam/Desktop/MY_UC_BERK/CHALLENGES/CHALLENGE_3/Starter_Code/PyPoll/Resources/election_data.csv')
#Initializing empty lists
candidates = []
all_candidates = []
percent_list = []
data = {}
total = 0

with open(election_data) as csvfile:
    #Reads file
    csvreader = csv.reader(csvfile)
    #Loops through file
    for row in csvreader:
        total += 1
        all_candidates.append(row[2])
        if row [2] in candidates:
            continue
        else:
            candidates.append(row[2])
    total -= 1

for i in range(1,len(candidates)):
    count = 0
    for j in range(len(all_candidates)):
        if candidates [i] == all_candidates[j]:
            count += 1
    data[candidates[i]]= count

candidates.remove(candidates[0])

#Prints results
print("Election Results")
print("-------------------------")
print("Total Votes: %d " %total)
print("-------------------------")
for i in candidates:
    percentage = (data[i] / total) * 100
    percent_list.append(percentage)
    print("%s : %.3f%% (%d) " % (i,percentage,data[i]))
print("-------------------------")
print("Winner: ", candidates[percent_list.index(max(percent_list))])
print("-------------------------")