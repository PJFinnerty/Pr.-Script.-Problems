# Method one for writing a file

#with open('slow.txt', 'r') as f:
#    print(f.tell())

import sys

print(sys.argv)
print(type(sys.argv))


numChars = 0   
    
with open('slow.txt', 'r') as f:
    for line in f:
        data = f.read( )
        chars = len(data)
        print(chars)

    
#f.write("\nHello, from the line!")
#print(f.tell())
    
#Weekly task 7
#Write a program that reads in a text file and outputs the number of e's it contains. 
#The program should take the filename from an argument on the command line.