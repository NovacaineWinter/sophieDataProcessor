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
		print 'Data in row '+str(i)		# print out i, but we have to tell python it is a string, otherwise it will try to perform an addition 
		print row		#print out the data that we have in row
		print ' '
		print 'First field: '+ row[0]
		print 'Second field: '+ row[1]
		print 'Third field: '+ row[2]		#note the zero index !
		print 'Fourth field: '+ row[3]
		print 'Fifth field: '+ row[4]
		print 'Sixth field: '+ row[5]
		print 'Seventh field: '+ row[5]
		print 'End for data for row '+str(i)
		print ' '
		print ' '
	i+=1				#add 1 on to i for each time through the loop

