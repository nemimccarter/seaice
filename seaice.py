import csv 
import matplotlib.pyplot as plt 

seaice_file = open('seaice.csv')
file_reader = csv.reader(seaice_file) # reader object
seaice_data = list(file_reader) # dictionary of csv data

extent_yearly_avg = 0
yearly_avg_dict = {} # [[year, avg_extent]] for graph
current_year = 0 # for comparison
yearly_sum = 0 # for averaging
extent_sum = 0 # for averaging

# set the current year to first year in csv (csv is chronological)
if (current_year == 0):
    current_year = seaice_data[0][0]

#calculate yearly average of extent
# index method: for index in range(len(seaice_data)):
for entry in seaice_data:
    if (entry[0] == current_year):
        yearly_sum = yearly_sum + 1
        extent_sum = extent_sum + float(entry[3])
    else:
        # year has been totaled. clear/update counters
        extent_yearly_avg = extent_sum / yearly_sum
        yearly_avg_dict[current_year] = extent_yearly_avg
        yearly_sum = 0
        extent_sum = 0
        current_year = entry[0]
plt.plot(yearly_avg_dict.values())
plt.ylabel("Average Extent")
plt.show()
