# Nemi McCarter-Ribakoff
# Analysis of sea ice extent from 1978 to 2015

import csv
extent_sum = 0   # sum of all extents in a year
num_years = 0    # number of data points in each year
extent_avg = []  # average annual extent =
                 #  extent_sum / num_years
list_years = []
list_extents = []
avg_index = 0       # index for extent average array

with open('seaice.csv', 'r') as csv_file:
    # skip the headers
    next(csv_file)

    # create lists of rows Year and Extent
    for row in csv_file:
        list_years.append(row[0])
        list_extents.append(row[3])

    # TODO: skip first row somehow -- they are strings
    current_year = list_years[0]
    for i in list_years:
        # take care of first row
        if (list_years[i] == current_year):
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
