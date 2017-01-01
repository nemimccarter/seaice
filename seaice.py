# Nemi McCarter-Ribakoff
# Analysis of sea ice extent from 1978 to 2015

import csv
file = open('seaice.csv')
csv_file = csv.reader(file)

extent_sum = 0   # sum of all extents in a year
num_years = 0    # number of data points in each year
extent_avg = []  # average annual extent =
                 #  extent_sum / num_years
list_years = []
list_extents = []
avg_index = 0       # index for extent average array
# create lists of rows Year and Extent
for row in csv_file:
    list_years.append(row[0])
    list_extents.append(row[3])

current_year = list_years[0]
for i in list_years:
    if (list_years[i + 1] == current_year):
        num_years += 1
        extent_sum += list_extents[i + 1]
    else:
        extent_avg[avg_index] = extent_sum / num_years
        avg_index += 1
        # clear out counters
        extent_sum = 0
        num_years = 0
for i in extent_avg:
    print extent_avg[i]
