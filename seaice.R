# Nemi McCarter-Ribakoff
# Analysis of daily extent sea ice 1978 to 2015

# import csv
seaice.dat <- read.csv("seaice.csv", header = TRUE)
num.years <- 2015 - 1978
extent.xbars <- vector(mode = "integer", length = num.years)
extent.sum = 0
current.year <- 0
index = 0

for (year in seaice.dat$Year) {
    current.year <- year
    while (current.year == year) {
      # add up all extent values in each year
      sum <- sum + seaice.dat
      # count up number of extent measurements
      index <- index + 1
    } 
    # store the mean
    extent.xbars[year] <- sum / index
    # do it all again
    index <- 0
    sum <- 0
}