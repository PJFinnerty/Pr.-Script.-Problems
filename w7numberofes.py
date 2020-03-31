#Peter Finnerty - Week 7 Task.

#Write a program that reads in a text file and outputs the number of e's it contains.
#The program should take the filename from an argument on the command line.
#---------------------------------------------------------------------------------

#Import sys
import sys

#Inform user of program name and text file to be investigated.
print("The name of this file is: " +sys.argv[0] +
", it is designed to investigate the text file 'moby-dick.txt'. "+ "\n")

Argument = input("Enter text file name: ")

#Use 'if' statement to ensure user enters correct file name.
if Argument != "moby-dick.txt":
    print("Incorrect filename")

#Create variables U and L and assign them to the values of 'E' and 'e'.
#Creat variables U2 and L2 - to be used in 'for' loops.
else:
    U = "E"
    L = "e"
    U2 = 0
    L2 = 0
    
    #Open the text file as f and read in file by line.
    with open("moby-dick.txt", 'r') as f:
        for line in f:
          #Split lines and assign this the variabele 'words'.
            words = line.split()
            #Create 'for' loop to iterate through each split element (or 'word') and 
            # assign this operation as 'i'.
            for i in words:
              #Create 'for' loop to iterate through each letter in each word.
              #Use variables U and L in conjunction with U2 and L2  to increment by 1 everytime
              # an 'E' or an 'e' is found.
                for letter in i:
                    if (letter == U ):
                      U2 = U2 + 1
                    if (letter == L):
                      L2 = L2 +  1
                    #Create variable to calculate combined no. of upper and lowercase e's.
                    Combined = U2 + L2

   #Print to the screen, the final result of U2 (E's) and L2 (e's).
   #Also print their combined total (as 'Combined').
    print ("\n" + "Occurrences of the uppercase letter 'E':      ", U2)
    print ("Occurrences of the lowercase letter 'e':    ", L2)
    print ("Occurances of both uppercase and lowercase: ", Combined)

#Complete.

#information on splitting lines into 'words' and 'letters' found @
#https://www.sanfoundry.com/python-program-read-file-counts-number/

#Information sys and it's uses found @
#https://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script

#Other means explored in counting individual characters found @
#https://www.youtube.com/watch?v=1uA-pLITer0




    






#example found at https://www.youtube.com/watch?v=MeocRDdeIQ8
# https://www.youtube.com/watch?v=w33xQBGdBzk


#filename = "moby-dick.txt"
#linecount = 0

#with open('moby-dick.txt', 'r') as f:
 #   for i in f:
  #      linecount = linecount + 1

#print(linecount)


#Example found at https://pythonexamples.org/python-count-number-of-characters-in-text-file/
#open file in read mode
#file = open("C:\data.txt", "r")

#read the content of file
#data = file.read()

#get the length of the data
#number_of_characters = len(data)

#print('Number of characters in text file :', number_of_characters)