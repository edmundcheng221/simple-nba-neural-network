import csv
import json

csvfile = open('nba-2021.csv', 'r')
jsonfile = open('nba-2021.json', 'w')

fieldnames = ("Visitor","Visitor pts","Home","Home pts","Winner")
reader = csv.DictReader( csvfile, fieldnames)
for i,row in enumerate(reader):
    if i == 0:
        jsonfile.write('[')
    else:
        json.dump(row, jsonfile)
        jsonfile.write(',\n')
jsonfile.write(']')

# If 0, the visiting team won
# If 1, the home team won