import os
import csv

input_path = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('analysis', 'election_analysis.txt')

candidates = {} # dictionary of candidates
total_votes = 0 # set starting vote count to 0

with open (input_path) as csvfile:

    reader = csv.reader(csvfile) # read rows (default delimiter is comma)
    headers = next(reader) # save headers row separately
    for row in reader: # loop through remaining rows
        current_candidate = row[2] # get current candidate  
        try:
            candidates[current_candidate] # refer to the key:value pair matching the current candidate
        except:
            candidates.update({current_candidate: 0}) # if no matching key:value pair, create key with value = 0
        candidates[current_candidate] = candidates[current_candidate] + 1 # increment value (vote) for each row matching current candidate (key)
        total_votes = total_votes + 1 # increment total votes for each row counted

#output to terminal and file
text = [] # list of lines to write as output
text.append("")
text.append("Election Results")
text.append("")
text.append("-------------------------")
text.append("")
text.append(f"Total Votes: {total_votes}")
text.append("")
text.append("-------------------------")
text.append("")
for name in candidates.keys():
     text.append(f"{name}: {round(int(candidates.get(name))/total_votes*100,3)}% ({candidates.get(name)})")
     text.append("")
text.append("-------------------------")
text.append("")
text.append(f" Winner: {max(candidates, key=candidates.get)}")
text.append("")
text.append("-------------------------")

with open (output_path, 'w') as f:
        f.writelines('\n'.join(text)) # write lines to file with newline character
        print('\n'.join(text)) # write lines to stout with newline character