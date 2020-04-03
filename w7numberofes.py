#Peter Finnerty - Week 7 Task.

#Write a program that reads in a text file and outputs the number of e's it contains.
#The program should take the filename from an argument on the command line.

#   λ w7numberofes.py
#   C:\Users\finne\Desktop\Scripting\w7numberofes.py is designed to count 
#   occurances of the letter 'e' in a text file.

#   Enter a text file name: w7moby-dick.txt

#   Occurrences of the uppercase letter 'E':       1363
#   Occurrences of the lowercase letter 'e':     116960
#   Occurances of both uppercase and lowercase:  118323
#---------------------------------------------------------------------------------

#Import sys
import sys

#Inform user of program name and function.
print (sys.argv[0], "is designed to count occurances of the letter 'e' in a text file.", "\n")

#Prompt user to input their chosen file.
Arg = input("Enter a text file name: ")

#Create variables U and L and assign them to the values of 'E' and 'e'.
#Creat variables U2 and L2 - to be used in 'for' loops.
U = "E"
L = "e"
U2 = 0
L2 = 0
Combined = U2 + L2
   
#Open input file as 'f' and read in file by line.
with open(Arg, 'r') as f:
    for line in f:
        #Split lines and assign this the variabele 'words'.
        words = line.split()
        #Create 'for' loop to iterate through each split element (or 'word').
        for i in words:
         #Create 'for' loop to iterate through each letter in each word.
         #Use variables U and L in conjunction with U2 and L2 and increment by 1 everytime
         # an 'E' or an 'e' is found.
            for letter in i:
                if (letter == U ):
                    U2 = U2 + 1
                if (letter == L):
                    L2 = L2 +  1
                #Create variable to calculate combined no. of upper and lowercase e's.
                Combined = U2 + L2

   #Print to the screen, the number if E's and then of e's.
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