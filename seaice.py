# Nemi McCarter-Ribakoff
# Analysis of sea ice extent from 1978 to 2015

import csv
file = open('seaice.csv')
csv_file = csv.reader(file)

for row in csv_file:
    print row
