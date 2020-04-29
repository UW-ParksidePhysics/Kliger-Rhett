# Modify the program from Exercise 4.1 such that the Fahrenheit temper-ature is read from a file with the following content:
# Temperature data
# ----------------
# Fahrenheit degrees:
# Rhett Kliger
infile = open('temperature.dat', 'r')
for i in range(0, 3):
    infile.readline() # Execute this line 3 times because we have 3 lines under the initial? Does nothing with the data.

F = float(((infile.readline()).split())[2])
infile.close()
C = (5.0/9) * (F - 32)
print(C)

