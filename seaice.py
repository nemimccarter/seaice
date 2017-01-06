import csv

seaice_file = open('seaice.csv')
file_reader = csv.reader(seaice_file) # reader object
seaice_data = list(file_reader) # dictionary of csv data
#format: seaice_data[row][col]
for row in seaice_data:
    print(row[0] + ' ' + row[3]) #prints year and extent
