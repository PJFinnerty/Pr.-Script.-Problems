# Scripting Respository
## About
This project focuses on 7 weekly tasks that I have completed as part of the Progamming and Scripting Module. This module forms part of the Higher Diploma in Data Analystics in GMIT. Weekly task 1 is not included in this repository as it did not involve creating a script. As such, the files contained herein are from Weekly Task 2 to Weekly Task 8 inclusive. The repository also contains supplementary files.

## Context and Progress
The weekly tasks that have been assigned throughout the semester relate to the fundamental
programming knowledge required to utilise Python efficiently. The programs created in completing these tasks range in complexity from a BMI calculator script that contains input functions and simple calculations, to a program that reads in a text file from the command line and counts the number of specific alphanumeric characters that it contains.
It is intended that in completing these tasks, an understanding of the principles and 
application of Python has been demonstrated. In addition to this, it is hoped that a consistency of work has been achieved, in both how the scripts have been refined, but also in how transparent the function of these programs has been made (through the use of concise comments and code sourcing).

## Contents and File Details
- **'gitignore' -** List of files to be ignored by git. 

- **'LICENCE' -** MIT Licence details. 

- **'practicefunction.py' -** This is a practice file, created to test the mechanics of approximating a square root. Each weekly task necessitated the creation of practice files in order to refine an inital script into efficient code. It has been included as an example.

- **'README.md -** This 'readme' file, which summarises the project.

- **'w2bmi.py' -** Week 2 Task - A simple script designed to calculate BMI. Learning outcomes from this task were the understanding of basic computing shortcuts in Python as well as utilisation of the 'input' and 'print' functions.  

- **'w3colourlessstrings.py' -** Week 3 Task - This program prompts the user for a string as input and returns the string in reverse order skipping every second letter. Basic indexing skills are used in the creation of this script.

- **'w4ifelse.py' -** Week 4 Task - A short script that takes an input and carries out a specific calculation based on whether the input is an odd or even number. This demonstrates a basic understanding of 'if' and 'while' loops and more importantly underscores the application of the iterative process. Outputs are modified to appear on the same line(s) by removing the end of line characters.

- **'w5weekdays.py' -** Week 5 Task - This program informs the user whether or not 'today' is a weekday or not. It utilises a data structure to do this. The script is designed to match the return of the current day (as indexed by the 'datetime' module) with a key from a provided dictionary.

- **'w6functions.py' -** Week 6 Task - The function 'sqrt' is created and used to calculate the approximate square root of a number input by the user. The Babylonian method (the repeated refinement of an inital guess) is used to do this by codifying the following formula into the script: 'x1 = (x0 + S / x0) / 2'.

- **'w7moby-dick.txt' -** A simple text file used to test the functionality of Week 7 Task.

- **'w7numberofes.py' -** Week 7 Task -  A program that takes a text file path as an argument from the command line and reads through the text. The 'sys' module reads in the file name to the command line. Secondly, the new line character ("\n") is used to space lines on the command line as appropriate. The program then splits each line of the text file into words, and using a more complicated compound of 'for' and 'if' loops, it breaks each word into individual characters and counts the amount of lower and upper case e's.

- **'w8plots.py' -** Week 8 Task - This script displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes. The 'numpy' module is imported to create the required range. Each function is plotted separately, all onto the same plot. Each line is assigned a colour and formatted individually according to colour and linewidth. Finally specifications are provided to the plot format: labels are applied the X and Y axes, a legend is created and a grid in the background.

## Credits
**w4ifelse.py**: 

- https://stackoverflow.com/questions/3249524/print-in-one-line-dynamically

**w5weekdays.py**: 

- https://stackoverflow.com/questions/19167276/pythonic-simplest-way-to-create-range-of-weekday-date-objects

**w6functions.py**:

- https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html

- https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d

- https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
 
**w7numberofes.py**:

- https://www.sanfoundry.com/python-program-read-file-counts-number/

- https://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script


## Copyright
This project is licensed under the terms of the MIT license and protected by Udacity Honor Code and Community Code of Conduct. See license and disclaimer.