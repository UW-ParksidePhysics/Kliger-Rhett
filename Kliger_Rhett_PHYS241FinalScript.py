#Final Script
#Rhett Kliger

# Overview
import matplotlib.pyplot as plt
import two_column_text_read_00 as tctr
import plot_data_with_fit_00
import lowest_eigenvectors_00
import univariate_statistics_00 as us
import fit_curve_array_00
import quadratic_fit_00
import equations_of_state
import matplotlib.pyplot as np

filename = 'Ge.Fd-3m.GGA-PBEsol.volumes_energies.dat'
display_Graph = True
my_eos = 'birch-murnaghan'
potential_name = 'square'
number_of_dimensions = 100
potential_parameter = 200


# Fit an Equation of a State

# 1. Extract the chemical symbol denoted by (CS), crystal symmetry symbol (CSS), density functional exchange-correlation approximation acronym denoted (AA) from your given data file's name.
# Write a function in your main script file called parse_file_name to return these three strings from the file name.
def parse_file_name(filename):
    to_parse = filename.split('.')
    CS, CSS, AA = to_parse[0:3]
    print(to_parse[0:3])
    return CS, CSS, AA

# 2. Read in data using two_column_text_read
data = tctr.two_column_text_read(filename)
print('Data Read In:')
print(data)

# 3. Divide by 2 because Fd3m
data1 = data/2
print(data1)

# 4. Pull out statistics using univariate_statistics module
statistics = us.univariate_statistics(filename)
print('Statistics of Data from File:')
print(statistics)


# Bohr is unit of length, Rydberg is unit of energy,
# First column is volumes, second column is energies
#def convert_units(data):
    #return data[0]/data[1]  # Data 0 is volumes, data 1 is energies




