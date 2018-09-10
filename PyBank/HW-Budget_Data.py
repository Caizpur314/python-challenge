# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 08:26:43 2018

@author: caeaizpu
"""

file = r'C:\Users\CAEAIZPU\Documents\Projects\python-challenge\PyBank\budget_data.csv'

import csv


with open(file) as budget_data:
    reader = csv.reader(budget_data)

    next(reader) 
    profit_losses = []
    date = []
    rev_delta = []

    # Sum of columns
    for row in reader:

        profit_losses.append(float(row[1]))
        date.append(row[0])

    
    #Calculation of average chenge and its corresponding dates  
    for i in range(1,len(profit_losses)):
        rev_delta.append(profit_losses[i] - profit_losses[i-1])   
        avg_rev_delta = sum(rev_delta)/len(rev_delta)

        max_rev_delta = max(rev_delta)

        min_rev_delta = min(rev_delta)

        max_rev_change_date = str(date[rev_delta.index(max(rev_delta))])
        min_rev_change_date = str(date[rev_delta.index(min(rev_delta))])

   
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(profit_losses))
    print("Avereage Revenue Change: $", round(avg_rev_delta))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_delta,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_delta,")")


out_file = r"C:\Users\CAEAIZPU\OneDrive - kochind.com\Desktop\Python HW-1\budget_data.txt"





