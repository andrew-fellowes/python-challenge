import os
import csv

input_path = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('analysis', 'budget_analysis.txt')

ppl = 0 # set starting previous P/L to 0
tpl = 0 # set starting total P/L  to 0
months = 0 # set starting month count to 0
cpl_list = [] # list to store all P/L changes
max_cpl = 0 # set starting max profit increase to 0
date_max_cpl = 0 # set start value for date of max profit increase
min_cpl = 0 # set starting max profit decrease to 0
date_min_cpl = 0 # set start value for date of max profit decrease

with open (input_path) as csvfile:
    reader = csv.reader(csvfile) # read rows as lists (default delimiter is comma)
    headers = next(reader) # save headers row separately
    for row in reader: # loop through remaining rows
        date = row[0] # current date
        pl = int(row[1]) # current P/L
        months = months + 1 # increase month count by 1 for each row processed
        tpl = tpl + pl # total P/L = total P/L + current P/L
        cpl = (ppl - pl) * -1 # P/L change = -(previous P/L - current P/L)
        cpl_list.append(int(cpl)) # add each P/L change to the list
        if cpl > max_cpl: # if it is the most positive seen ...
            max_cpl = cpl # ... store the current P/L change ...
            date_max_cpl = row[0] # ... and store it's date
        if cpl < min_cpl: # if it is the most negative seen ...
            min_cpl = cpl # ... store the current P/L change ...
            date_min_cpl = row[0] # ... and store it's date
        ppl = pl # set previous P/L to current P/L before beginning next loop
cpl_list.pop(0) # remove the first P/L change because it is based on an arbitrary previous P/L

# output to terminal and file
text = [] # list of lines to write as output
text.append("")
text.append("Financial Analysis")
text.append("")
text.append("----------------------------")
text.append("")
text.append(f"Total Months: {months}")
text.append("")
text.append(f"Total: ${tpl}")
text.append("")
text.append(f"Average Change: ${round(sum(cpl_list)/len(cpl_list),2)}") # round percent change to 2 decimals
text.append("")
text.append(f"Greatest Increase in Profits: {date_max_cpl} (${max_cpl})")
text.append("")
text.append(f"Greatest Decrease in Profits: {date_min_cpl} (${min_cpl})")
text.append("")
with open (output_path, 'w') as f:
    f.writelines('\n'.join(text)) # write lines to file with newline character
    print('\n'.join(text)) # write lines to stout with newline character