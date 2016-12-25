# Nemi McCarter-Ribakoff
# Analysis of sea ice extent from 1978 to 2015

import csv
with open('seaice.csv', newline=' ') as csvfile:
	seaice = csv.reader(csvfile, delimiter=' ', quotechar='|')
	
