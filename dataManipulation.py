import csv
import sys


def getUniqueRiceLines(data):
	#loop through to get all the names of the rice into one big long list
	allRice = []
	for i in range(0,len(data)):
		allRice.append(data[i][2])

	uniqueRice = list(set(allRice))			#set is a data structure that cannot have duplicates in, turn it into a set then turn it back into a list

	return uniqueRice



def parseDataInput(data):
	allData = []
	for row in data:
		allData.append(row);

	return allData


def isNum(input):
	try: 
		float(input)
		return True
	except:
		return False


# sys.argv[1] is the file location passed over command line
	#open reads the file passed into the var f. 
	#'rU' is read Universal. read as opposed to write, Universal is allowing for maximum compatibility with each csv format
f = open(sys.argv[1], 'rU')


#pass the file to the csv reader 
data = csv.reader(f)


#this is the percentile for choosing the data
print "Enter percentile to filter by as an integer i.e 95% as 95"
percentile = float(float(int(input()))/100);

allData = parseDataInput(data)

uniqueRice = getUniqueRiceLines(allData)





print 'Detected ' + str(len(uniqueRice)) +' rice types'


"""
	Create the places we are going to store data 
"""

dataStore = {} # create a place to store the data
maxVals = {}	#here we will store the maximum gs values for each rice in order to work out 95%
dataOutput = {}

for i in range(0,len(uniqueRice)):
	dataStore[uniqueRice[i]] = [[],[],[],[],[],[]] 	#create an empty list called by the name of the rice 
	
	dataOutput[uniqueRice[i]] = [[],[],[],[],[],[]] 	#create an empty list called by the name of the rice 
	
	maxVals[uniqueRice[i]] = [0,0,0,0,0,0] 	#create an zero var for storing the max gs values for each  





#insert the data points 
for i in range(1,len(allData)):
	dataindex = (int(allData[i][3])-1)
	dataStore[allData[i][2]][int(allData[i][3])-1].append(allData[i])



for i in range(0,len(uniqueRice)):

	thisRice = uniqueRice[i]		#goes through each rice in turn
	for k in range(0,6):		
		numDataPoints = len(dataStore[thisRice][k])
		for j in range(0,numDataPoints):

			if(isNum(dataStore[thisRice][k][j][5])):
				if( float(dataStore[thisRice][k][j][5]) > maxVals[thisRice][k] ):
					#print 'new high found for '
					maxVals[thisRice][k] = float(dataStore[thisRice][k][j][5])

		dataStore[thisRice][k] = sorted(dataStore[thisRice][k], key=lambda k: float(k[1]))




#we now have the data segmented up by rice, and we have the maximum gs values for each
#lets go through again and find out which ones are below 95%

for i in range(0,len(uniqueRice)):


	thisRice = uniqueRice[i]		#goes through each rice in turn
	for k in range(0,6):

		carryingOn = True;

		for j in range(0,len(dataStore[thisRice][k])):

			if(isNum(dataStore[thisRice][k][j][5])):

				if(float(dataStore[thisRice][k][j][5]) < (float(maxVals[thisRice][k] * percentile)) and carryingOn):

					dataOutput[thisRice][k].append( dataStore[thisRice][k][j])

				else:
					carryingOn = False;
			else:
				
				dataOutput[thisRice][k].append( dataStore[thisRice][k][j])


	#print str(len(dataStore[thisRice]))+' data points in rice '+ thisRice +', max val:'+str(maxVals[thisRice])



toCSV = []

for i in range(0,len(uniqueRice)):

	thisRice = uniqueRice[i]

	for k in range(0,6):

		for j in range(0,len(dataOutput[thisRice][k])):
			toCSV.append(dataOutput[thisRice][k][j])

print str(len(allData))+' data points imported '+str(len(toCSV)) +' data points exported to export.csv, '+str(len(allData) - len(toCSV))+' removed'

with open('export.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(toCSV)

csvFile.close()



