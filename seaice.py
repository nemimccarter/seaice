import csv
import matplotlib.pyplot as plt

seaice_file = open('seaice.csv')
file_reader = csv.reader(seaice_file) # reader object
seaice_data = list(file_reader) # dictionary of csv data
years = []
extents = []
#format: seaice_data[row][col]
#extract each extent and year taken
for row in seaice_data:
    years.append(row[0])
    extents.append(row[3])
plt.plot(extents)
plt.ylabel('Extent')
plt.show()
