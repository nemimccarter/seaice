import csv
import matplotlib.pyplot as plt

seaice_file = open('seaice.csv')
file_reader = csv.reader(seaice_file) # reader object
seaice_data = list(file_reader) # list of csv data
# seaice_data.sort()
years = []
extents = []
extent_yearly_avg = []
#format: seaice_data[row][col]
#extract each extent and year taken
for row in seaice_data:
    years.append(row[0])
    extents.append(row[3])
#calculate yearly average of extent
current_year = years[0]
extent_yearly_sum = 0 # to be averaged
year_count = 0        # to be averaged
for index in range(len(years)):
    if (years[index] == current_year):
        extent_yearly_sum = extent_yearly_sum + float(extents[index])
        year_count = year_count + 1
    else:
        # we've added up all the measurements for this year
        #calculate year's average extent
        extent_yearly_avg.append(extent_yearly_sum / year_count)
        # zero out counters
        year_count = 0
        extent_yearly_sum = 0
        # update index and current year
        current_year = years[index]
plt.plot(extent_yearly_avg)
plt.ylabel('Average Annual Extent')
plt.show()
