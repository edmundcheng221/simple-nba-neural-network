import csv
import json

csvfile = open('nba-2021.csv', 'r')
jsonfile = open('nba-2021.json', 'w')

fieldnames = ("Visitor","Visitor pts","Home","Home pts")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
