import os
import csv

input_path = os.path.join('..', 'Resources', 'budget_data.csv')

with open (input_path) as csvfile:
    csvreader - csv.reader(csvfile, delimiter=',')
    next(reader, None)
    for row in csvreader:
        