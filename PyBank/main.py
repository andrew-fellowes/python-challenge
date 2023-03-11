import os
import csv

input_path = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('analysis', 'budget_analysis.txt')

ppl = 0 # setting starting previous profit/loss to 0
tpl = 0 # setting starting total profit/loss  to 0
months = 0 # setting starting month count to 0
cpl_accumulator = [] # list to store all profit/loss changes
max_cpl = 0 # setting starting max profit increase to 0
date_max_cpl = 0 #setting start value for date of max profit increase
min_cpl = 0 # setting starting max profit decrease to 0
date_min_cpl = 0 # setting start value for date of max profit decrease

with open (input_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        date = row[0]
        pl = int(row[1]) # current profit/loss
        months = months + 1 # increase month count by 1 for each row processed
        tpl = tpl + pl # total profit/loss = total profit/loss + current profit/loss
        cpl = (ppl - pl) * -1 # change in profit/loss = -(previous profit/loss - current profit loss)
        cpl_accumulator.append(int(cpl))
        if cpl > max_cpl:
            max_cpl = cpl
            date_max_cpl = row[0]
        if cpl < min_cpl:
            min_cpl = cpl
            date_min_cpl = row[0]
        ppl = pl # set previous profit/loss to current profit/loss before beginning next loop
cpl_accumulator.pop(0) # remove the first change in profit/loss because it is based on an arbitrary previous profit/loss amount

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
text.append(f"Average Change: ${round(sum(cpl_accumulator)/len(cpl_accumulator),2)}")
text.append("")
text.append(f"Greatest Increase in Profits: {date_max_cpl} (${max_cpl})")
text.append("")
text.append(f"Greatest Decrease in Profits: {date_min_cpl} (${min_cpl})")
text.append("")
with open (output_path, 'w') as f:
    f.writelines('\n'.join(text))
    print('\n'.join(text))