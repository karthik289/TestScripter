import json

import csv

f = open('employee_data.json')
response_data = json.load(f)
f.close()
carrier['']
response_parsed = json.loads(employee_data)

csv_data = employee_parsed['items']

# open a file for writing

employ_data = open('EmployData.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(employ_data)

count = 0

for csvdata in csv_data:

      if count == 0:

             #header = emp.keys()
             csvdata['carrier'].keys();
             
             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(emp.values())

employ_data.close()


