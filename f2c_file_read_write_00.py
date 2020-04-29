#Exercise 4.4: Read and write several numbers from and to file
# Rhett Kliger


infile = open('temperature2.dat', 'r')
for i in range(0, 3):
    infile.readline()  # Reading the lines in temperature2.dat only reading. Basically skipping them
for line in infile:
    F = float(line.split()[2])
    C = (5.0/9) * (F - 32)
    print('%f %f' %(F, C))
