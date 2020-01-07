#!/bin/python


import csv
import json

csvfile = "ibe-cd-input.csv"
jsonfile = "nodes.json"

arr = []

with open(csvfile) as csvfile:
    csvReader = csv.DictReader(csvfile)
    for row in csvReader:
         arr.append(row)

print(arr)

output = { "nodes": arr}

with open(jsonfile,"w") as jsonfile:
    jsonfile.write(json.dumps(output, indent = 2))