#Exercise 4.5: Use exceptions to handle wrong input
# Rhett Kliger

import sys

try:
    F = float(input(sys.argv[1]))
except IndexError:
    print('You failed to provide a temperature in Fahrenheit as input on the command line!')
    sys.exit(1)
C = 5/9 * (F - 32)
print("%g Fahrenheit = %g Celsius" % (F, C))
