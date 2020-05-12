# Read two columns
import numpy as np
def two_column_text_read(filename):


    filename = 'Ge.Fd-3m.GGA-PBEsol.volumes_energies.dat'
    print()
    while True:
        try:
            infile = open(filename, 'r')
            break
        except OSError:
            print('This file is not found.')

    x = []
    y = []

    for line in infile:
        content = line.split()
        x.append(float(content[0]))
        y.append(float(content[1]))
    infile.close()

two_column_text_read("hello")














