#Create a script to analyze poll data by caculating the following:
#Total number of votes cast
#A complete list of candidates
#The percentage of Votes Each candidates Won
#The total number of vote for each candidate
#Winner 

import os
import csv

#Define variables
votes = 0
vote_count = []
candidates = []
csv_reader = ['1','2']

# Pull in data & read file
csvpath = os.path.join("C:/Users/Tiffa/Documents/python-challenge/PyPoll/Resources/election_data.csv")
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader)

    for row in csv_reader:
        #Tally votes
        votes = votes + 1
        #Candidates
        candidate = row[2]
        #Votes per candidate
        if candidate in candidates:
           candidate_index = candidates.index(candidate)
           vote_count[candidate_index] = vote_count[candidate_index] + 1
        else:
           candidates.append(candidate)
           vote_count.append(1)
#Percentages
percentages = []
most_votes = vote_count[0]
most_votes_index = 0
for count in range(len(candidates)):
    vote_percentage = vote_count[count]/votes*100
    percentages.append(vote_percentage)
    if vote_count[count] > most_votes:
        print(most_votes)
        most_votes_index = count
winner = candidates[most_votes_index]
percentages = [round (i,2) for i in percentages]
#Print results           
print()
print("Election Results")
print("--------------------------------")
print(f"Total Votes: {votes}")
print("--------------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})")
print("--------------------------------")
print(f"Winner:  {winner}")
print("--------------------------------")
 

 #open a file for writing:
f = open("C:/Users/Tiffa/Documents/python-challenge/PyPoll/analysis/poll.txt","w")
print("Election Results", file=f)
print("--------------------------------", file=f)
print(f"Total Votes: {votes}", file=f)
print("--------------------------------", file=f)
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})", file=f)
print("--------------------------------", file=f)
print(f"Winner:  {winner}", file=f)
print("--------------------------------", file=f)



f.close()
#Election Results
#Total Votes: 1048575
#Khan: 63.09% (661583)
#Correy: 19.94% (209046)
#Li: 13.96% (146360)
#O'Tooley: 3.01% (31586)
#Winner:  Khan