#Final Script
#Rhett Kliger

# Overview
import matplotlib.pyplot as plt
import two_column_text_read_00 as tctr
import plot_data_with_fit_00
import lowest_eigenvectors_00
import univariate_statistics_00 as us
import fit_curve_array_00
import quadratic_fit_00 as qf
import equations_of_state as eos
import matplotlib.pyplot as np

filename = 'Ge.Fd-3m.GGA-PBEsol.volumes_energies.dat'
display_Graph = True
my_eos = 'birch-murnaghan'
potential_name = 'square'
number_of_dimensions = 100
potential_parameter = 200
bulk_modulus = 77.2  # The bulk modulus of Germanium in GPa


# Fit an Equation of a State

# 1. Extract the chemical symbol denoted by (CS), crystal symmetry symbol (CSS), density functional exchange-correlation approximation acronym denoted (AA) from your given data file's name.
# Write a function in your main script file called parse_file_name to return these three strings from the file name.
def parse_file_name(filename):
    to_parse = filename.split('.')
    CS, CSS, AA = to_parse[0:3]
    print(to_parse[0:3])
    return CS, CSS, AA

# 2. Read in data using two_column_text_read X
data = tctr.two_column_text_read(filename)
print('Data Read In:')
print(data)

# 3. Divide by 2 because Fd3m X
data1 = data/2
print('Revised Data Based on Atoms:')
print(data1)

# 4. Pull out statistics using univariate_statistics module (Need Help)
#statistics = us.univariate_statistics(filename)
#print('Statistics of Data from File:')
#print(statistics)

# 5. Fit a quadratic polynomial using quadratic_fit module  X
quadratic_coefficients = qf.quadratic_fit(data1)
print('Quadratic Coefficients of Revised Data:')
print(quadratic_coefficients)

# 6. Pass quadratic coefficients and data into fit_eos function
volumes = data1[0]
energies = data1[1]
eos_passed_info = eos.fit_eos(volumes, energies, quadratic_coefficients, my_eos, number_of_points=50)
print('Fitted Data from File and Fitted Quadratic Coefficients: ')
print(eos_passed_info)

# 7. Define a function to covert received data from 6. from atomic units to cubic bohr/atom, rydberg/atom, and rydberg/cubic bohr
# Bohr is unit of length, Rydberg is unit of energy,
# First column is volumes, second column is energies
# Three arguments: the value to be converted, the units of the value to be converted from, the units to be converted to,
# function should RETURN the value in requested units
# (value_to_convert_from), (units_of_value_converted_from), (unit_to_convert_to)
def convert_units(value_to_convert_from, units_of_value_converted_from, unit_to_convert_to):
    if units_of_value_converted_from == 'cubic bohr/atom':
        value_in_requested_units = value_to_convert_from * 0.148185  # 1 cubic Bohr equals 0.148185 Angstrom
    elif units_of_value_converted_from == 'rydberg/atom':
        value_in_requested_units = value_to_convert_from * 13.606  # 1 Rydberg equals 13.606eV
    elif units_of_value_converted_from == 'rydberg/cubic bohr':
        value_in_requested_units = value_to_convert_from / 29421.0265
    else:
        value_in_requested_units = value_to_convert_from
    return value_in_requested_units






