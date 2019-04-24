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
	if i < 0:			# i only want to show the first 10 lines rather than thousands
	
		print row		#print out the data that we have in row
		
	i+=1				#add 1 on to i for each time through the loop

"""
the variable "row" is a list, lists can be accessed by their positions, which is what we did in the previous example, 
	for instance, we access the first position with row[0], the second by row[1] and so on

	instead of lists, we can use "dictionaries" which is pythons way of saying giving things names
"""

my_list = {}	#empty dict

my_list['sport'] = 'climbing'
my_list['favouritePet'] = 'dog'
my_list['age'] = 28		#can also have integers in
my_list['dogs'] = ['Monte','Benson']  # can also be a list

print " "		#get us some space in the terminal
print " "
print " "

print 'my favourite sport is ' + my_list['sport']
print " "

print "I am "+str( my_list['age'] ) + ' years old';
print " "
"""
print my_list



#	Dicts are a good way of keeping like data together - the key names are very very useful - we will 
#	exploit this with the names of your rice. other than the names, they behave exactly like their variable types

	
#	we can do more interesting things like this;


print " "
print "I have "+ str(  len(  my_list['dogs']  )  ) + ' dogs'



#even more cool, we can loop over a list when we know how long it is, using the len() function


namesOfMyDogs = ''   # empty string

for i in range(0,len(my_list['dogs'])):

	namesOfMyDogs+= my_list['dogs'][i]+', '

#we can now say...

print 'Their names are '+namesOfMyDogs





##	we can then add some other items to a list, even after we have done other stuff with it 


my_list['dogs'].append('jerry')
my_list['dogs'].append('Zebedee')

namesOfAllDogs = ''   # empty string

for i in range(0,len(my_list['dogs'])):

	namesOfAllDogs+= my_list['dogs'][i]+', '


print "but when we go "+ my_list['sport']+" we often have "+str(len(my_list['dogs']))+" dogs. All together we have "+namesOfAllDogs
"""