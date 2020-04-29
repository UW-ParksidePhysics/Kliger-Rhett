#Make a program that asks the user for a temperature in Fahrenheitdegrees and reads the number; computes the corresponding
# temperature in Celsius degrees; and prints out the temperature in the Celsius scale
# Rhett Kliger
from pip._vendor.distlib.compat import raw_input

F = raw_input('What is the temperature in degrees fahrenheit? ')
F = float(F)
C = 5/9*(F - 32)

print('Your temperature in degrees Celsius:', C)