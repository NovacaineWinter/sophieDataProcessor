import csv
import sys

# sys.argv[1] is the file location passed over command line
	#open reads the file passed into the var f. 
	#'rU' is read Universal. read as opposed to write, Universal is allowing for maximum compatibility with each csv format
f = open(sys.argv[1], 'rU')

#pass the file to the csv reader 
data = csv.reader(f)

#initialise a counter
i=0

for row in data:
	if i < 10:			# i only want to show the first 10 lines rather than thousands
		print row
	i+=1				#add 1 on to i for each time through the loop

