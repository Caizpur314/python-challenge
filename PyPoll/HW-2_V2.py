# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 14:41:27 2018

@author: caeaizpu
"""
file = r'C:\Users\CAEAIZPU\Documents\Projects\python-challenge\PyPoll\election_data (1).csv'

import csv


with open(file) as election_data:
    reader = csv.reader(election_data)

    next(reader) 
    Voter_ID =[]
    County =[]
    Candidate =[]

    # Sum of columns
    for row in reader:

        Voter_ID.append(str(row[0]))
        Candidate.append(str(row[2]))
        County.append(str(row[1]))

print("Total Voters:", len(Voter_ID))

Vote_Li = [person for person in Candidate if person == "Li"]
len(Vote_Li)/len(Candidate)

Vote_Li_2 = []
for person in Candidate:
    if person  == "Li":
        Vote_Li_2.append(person)
print(len(Vote_Li_2)/len(Candidate)*100)

print(len(Vote_Li_2))

Vote_Khan = []
for person in Candidate:
    if person  == "Khan":
        Vote_Khan.append(person)
print(len(Vote_Khan)/len(Candidate)*100)

print(len(Vote_Khan))

Vote_Correy = []
for person in Candidate:
    if person  == "Correy":
        Vote_Correy.append(person)
print(len(Vote_Correy)/len(Candidate)*100)

print(len(Vote_Correy))

Vote_Tooley = []
for person in Candidate:
    if person  == "O'Tooley":
        Vote_Tooley.append(person)
print(len(Vote_Tooley)/len(Candidate)*100)

print(len(Vote_Tooley))

if len(Vote_Khan) > len(Vote_Li_2) and len(Vote_Khan) > len(Vote_Correy) and len(Vote_Khan) > len(Vote_Tooley):
    winner = "Khan"
    print("Winner: {}".format(winner))
elif len(Vote_Li_2) > len(Vote_Khan) and len(Vote_Li_2) > len(Vote_Correy) and len(Vote_Li_2) > len(Vote_Tooley):
    winner = "Li"
    print("Winner: {}".format(winner))
elif len(Vote_Correy) > len(Vote_Khan) and len(Vote_Correy) > len(Vote_Li_2) and len(Vote_Correy) > len(Vote_Tooley):
    winner = "Correy"
    print("Winner: {}".format(winner))
elif len(Vote_Tooley) > len(Vote_Khan) and len(Vote_Tooley) > len(Vote_Li_2) and len(Vote_Tooley) > len(Vote_Correy):
    winner = "O'Tooley"
    print("Winner: {}".format(winner))


print("Election Results")
print("-----------------------------------")
print("Total Votes:", len(Voter_ID))
print("-----------------------------------")
print("Khan: ", str(round(len(Vote_Khan)/len(Candidate)*100,2)), "%", "(",len(Vote_Khan),")")
print("Correy: ", str(round(len(Vote_Correy)/len(Candidate)*100,2)), "%", "(",len(Vote_Correy),")")
print("Li:", str(round(len(Vote_Li_2)/len(Candidate)*100,2)), "%", "(",len(Vote_Li_2),")")
print("O'Tooley:", str(round(len(Vote_Tooley)/len(Candidate)*100,2)), "%", "(",len(Vote_Tooley),")")
print("-----------------------------------")
print("Winner: {}".format(winner))

  