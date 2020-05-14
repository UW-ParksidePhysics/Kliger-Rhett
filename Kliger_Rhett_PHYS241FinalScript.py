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
import statistics as st
import numpy as np

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


# Call the function
CS, CSS, AA = parse_file_name(filename)

# 2. Read in data using two_column_text_read X
data = tctr.two_column_text_read(filename)
print('Data Read In:')
print(data)

# 3. Divide by 2 because Fd3m X
data1 = data/2
print('Revised Data Based on Atoms:')
print(data1)

# 4. Pull out statistics using univariate_statistics module (Need Help) X
statistics = us.univariate_statistics(data1)
print('Statistics of Data from File:')
print(statistics)

# 5. Fit a quadratic polynomial using quadratic_fit module  X
quadratic_coefficients = qf.quadratic_fit(data1)
print('Quadratic Coefficients of Revised Data:')
print(quadratic_coefficients)

# 6. Pass quadratic coefficients and data into fit_eos function X

volumes = data1[:,0] # The : operator means all elements till the end.
energies = data1[:,1] # The :, means all in that column
eos_passed_info, eos_parameters = eos.fit_eos(volumes, energies, quadratic_coefficients, my_eos, number_of_points=50)
print('Fitted Data from File and Fitted Quadratic Coefficients: ')
print(eos_passed_info)
equilibrium_volume = eos_parameters[3]
bulk_modulus = eos_parameters[1]

# 7. Define a function to covert received data from 6. from atomic units to cubic bohr/atom, rydberg/atom, and rydberg/cubic bohr
# Bohr is unit of length, Rydberg is unit of energy,
# First column is volumes, second column is energies
# Three arguments: the value to be converted, the units of the value to be converted from, the units to be converted to,
# function should RETURN the value in requested units
# (value_to_convert_from), (units_of_value_converted_from), (unit_to_convert_to)
def convert_units(value_to_convert_from, units_of_value_converted_from, unit_to_convert_to):
    if units_of_value_converted_from == 'cubic bohr/atom':
        value_in_requested_units = value_to_convert_from * 0.148185  # 1 cubic Bohr equals 0.148185 cubic Angstrom
    elif units_of_value_converted_from == 'rydberg/atom':
        value_in_requested_units = value_to_convert_from * 13.606  # 1 Rydberg equals 13.606eV
    elif units_of_value_converted_from == 'rydberg/cubic bohr':
        value_in_requested_units = value_to_convert_from / 29421.0265
    else:
        value_in_requested_units = unit_to_convert_to
    return value_in_requested_units

# 8. Plot the data and the fit function with volume on the horizontal axis and energy on the vertical axis
# Need to make it so that max x values and min x values are 10% beyond max and min data points
# You should use raw strings (precede the quotes with an 'r'), and surround the math text with dollar signs ($)
eos_volumes = np.linspace(min(volumes), max(volumes), len(eos_passed_info))

print(eos_volumes)
plt.plot(volumes, energies, 'o', color='blue')
plt.plot(eos_volumes, eos_passed_info, color='black')
x_min = (min(volumes) - (0.1) * (max(volumes) - min(volumes)))
x_max = (max(volumes) + (0.1) * (max(volumes) - min(volumes)))
y_min = (min(energies) - (0.1) * (max(energies) - min(energies)))
y_max = (max(energies) + (0.1) * (max(energies) - min(energies)))
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel(r' $V$  [eV/atom] ')
plt.ylabel(r' $E$  [$\AA^3$/atom] ')


# 9. Write a function called annotate_graph to annotate the graph
# 'Numbers' are placeholders

def annotate_graph(CS, CSS, AA, bulk_modulus, equilibrium_volume, x_min, x_max, y_min, y_max): # If not add CSS
    x_range = x_max - x_min
    y_range = y_max - y_min
    x_CS = x_min + 0.05 * x_range #Coordinates of x for chemical symbol
    y_CS = y_max - 0.05 * y_range #Coordinates of y for chemical symbol
    x_CSS = x_min + x_range/2
    y_CSS = y_max - y_range/2
    x_K = x_min + x_range/2
    y_K = ((y_max - y_range/2) + 0.0005)
    print(AA)
    plt.title('Birch Murnaghan Equation of State for Ge in DFT GGA_PBEsol', y=1.05) # Move title up so no overlapping
    plt.text(x_CS, y_CS, CS)
    print(CSS)
    plt.text(x_CSS, y_CSS, r' $ \ Fd}$3$m} $')  # Had to do it this way for italics
    print(bulk_modulus)
    plt.text(x_K, y_K, r' $K_0$ =0.00456392914 GPa')  # Might need to change this with 'birch-murnaghan'
    #plt.text('number', 'number', 'V_0 =' + equilibrium_volume + r' $\mathit{AA^3/atom}\ $')
    #plt.text(left, bottom, 'Created By Rhett Kliger 2020-5-14', horizontalalignment='left', verticalalignment='top', transform=ax.transAxes)
    #return


annotate_graph(CS, CSS, AA, bulk_modulus, equilibrium_volume, x_min, x_max, y_min, y_max)

plt.show()
# 10.




