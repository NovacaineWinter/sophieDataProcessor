'''
Column numbers for reference:

R.AccGs.csv
  PAR | time | name  | rep # | leaf Width |  GS  |
   0  |  1   |   2   |  3    |      4     |   5  |


Pracha_data.csv
PAR | Time (sec) | Line | ADNID code | Accession | ADN code | Rep | Photo | cond | NPQ | ETR | WUE | Trmmol |
 0  |      1     |   2  |     3      |     4     |     5    |  6  |   7   |   8  |  9  |  10 |  11 |   12   |

'''

# filter percentage - 95% as 95
filterPercent = 95

# column positions in the csv
timeCol = 1
nameCol = 2
repCol = 3
filterCol = 5 #this is the dependant variable

saveOutASubset = True
numToSubset = 5

# file names
#inputFileName = '/home/matt/Desktop/testdata.csv' #assume in same directory as this code, unless you specify a separate pathway
#inputFileName = './Pracha_data.csv' #assume in same directory as this code, unless you specify a separate pathway
inputFileName = './R.AccGs.csv' #assume in same directory as this code, unless you specify a separate pathway
outputFileName = 'Pracha_data_filteredByPhoto.csv' #this will get dumpoed in your set working directory.