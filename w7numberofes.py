#Peter Finnerty
#Write a program that reads in a text file
#and outputs the number of e's it contains.
# The program should take the filename 
# from an argument on the command line.

#$ python es.py moby-dick.txt
#116960

filename = "moby-dick.txt"
linecount = 0

with open(moby-dick.txt, 'r') as f:
    for i in f:
        linecount = linecount + 1

print(linecount)


#Example found at https://pythonexamples.org/python-count-number-of-characters-in-text-file/
#open file in read mode
#file = open("C:\data.txt", "r")

#read the content of file
#data = file.read()

#get the length of the data
#number_of_characters = len(data)

#print('Number of characters in text file :', number_of_characters)