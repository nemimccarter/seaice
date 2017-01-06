import csv 
import matplotlib.pyplot as plt 

seaice_file = open('seaice.csv')
file_reader = csv.reader(seaice_file) # reader object
seaice_data = list(file_reader) # list of csv data
# seaice_data.sort() # place in chronological order
extent_yearly_avg = 0 # yearly avg extent = extent_sum / point_count
yearly_avg_dict = {} # [[year, [avg_extent, hemisphere]]] for graph
current_year = 0 # for comparison
point_count = 0 # for averaging
extent_sum = 0 # for averaging

# set the current year to first year in csv (csv is chronological)
current_year = seaice_data[0][0]

#calculate yearly average of extent
# index method: for index in range(len(seaice_data)):
for entry in seaice_data:
    if (entry[0] == current_year):
        point_count = point_count + 1
        extent_sum = extent_sum + float(entry[3])
    else:
        # year has been totaled. clear/update counters
        extent_yearly_avg = extent_sum / point_count
        yearly_avg_dict[current_year] = extent_yearly_avg
        point_count = 0
        extent_sum = 0
        current_year = entry[0]
plt.plot(yearly_avg_dict.values())
plt.plot(yearly_avg_dict.keys())
plt.ylabel("Average Extent")
plt.xlabel("Year")
plt.show()
