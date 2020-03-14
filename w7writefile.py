# Method one for writing a file

with open('w7myfile.txt', 'a') as f:
    print(f.tell())
    f.write("\nHello, from the line!")
    print(f.tell())
    
#Weekly task 7
#Write a program that reads in a text file and outputs the number of e's it contains. 
#The program should take the filename from an argument on the command line.