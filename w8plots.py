#Peter Finnerty - Week 8 Task

#Write a program that displays a plot of the functions 
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] 
# on the one set of axes.
#----------------------------------------------------------------

#Import numpy for arrays and matplotlib for plotting.
import numpy as np
import matplotlib.pyplot as plt

#Create a variable 'x' and assign the range.
x = np.arange(0.0, 4.0)

#Create the 3 funcions and substiute 'x' in.
def f(x): 
    return x

def g(x):
    return x * x

def h(x):
    return x **3

#Create  representation of the 3 functions, using the chosen
#label and linewidth formats.
plt.plot( f(x), 'b', label = 'f(x)', linewidth = 1.5)
plt.plot( g(x), 'r', label = 'g(x)', linewidth = 1.5) 
plt.plot( h(x),'g', label = 'h(x)', linewidth = 1.5)

#Add further plot details including line grids and legends.
#Information on specialised formatting from Edureka:
# @ https://www.youtube.com/watch?v=yZTBMMdPOww&list=PL9ooVrP1hQOHY-BeYrKHDrHKphsJOyRyu&index=68&t=0s
plt.title('Week 8 Task')
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.legend()
plt.grid(True, color = 'k')

#Use the show() function to ensure that the graph is always
#shown when the program is run.
plt.show()