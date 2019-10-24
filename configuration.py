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
repCol = 6
filterCol = 7

# file names
inputFileName = 'Pracha_data.csv'
outputFileName = 'Pracha_data_filteredByPhoto.csv'