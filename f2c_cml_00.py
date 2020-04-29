# Modify the program from Exercise 4.1 such that the Fahrenheit temperature is read from the command line
# Rhett Kliger
import sys

# sys.argv[0] is the argument that is of our current script
# I want to read from the command line of the script of the previous problem
# I need to use the terminal to do this, view, tool windows, terminal


try:
    F = float(sys.argv[1])
except:
    F = float(input('What is the temperature in degrees fahrenheit? '))

C = 5 / 9. * (F - 32)
print("%g Fahrenheit = %g Celsius" % (F, C))
