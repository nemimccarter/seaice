# seaice
A study on extent sea ice from 1975 to 2015. Working in R and Python for comparison.
The data comes courtesy of [The National Snow and Ice Data Center](https://nsidc.org/data/nsidc-0051 "The National Snow and Ice Data Center").

Currently all I want to do is some basic statistical analysis:
 - find and graph annual mean and median, compare the two
 - quantify trends -- when are the lows/highs, how does the annual trend change overtime
 - identify outliers based on most appropriate definition (will use boxplot for now because I am a noob)
 
Next, I want to make some prediction models and see which reaches the highest accuracy in the following scenarios:
 - Trained on all available data, tested on 2016
 - Trained on 1978 to 2009, tested on 2010 to 2016
 - Trained on 1978 to 2000, tested on 2001 to 2016
 
 More work TBD
 
 # Works Cited
 Cavalieri, D. J., C. L. Parkinson, P. Gloersen, and H. J. Zwally. 1996, updated yearly. Sea Ice Concentrations from Nimbus-7 SMMR and DMSP SSM/I-SSMIS Passive Microwave Data, Version 1. Boulder, Colorado USA. NASA National Snow and Ice Data Center Distributed Active Archive Center. doi: http://dx.doi.org/10.5067/8GQ8LZQVL0VL. Accessed 22 December 2016.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNjUwOTQ5NjNdfQ==
-->