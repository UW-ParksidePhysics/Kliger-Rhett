#Final Script
#Rhett Kliger

# Overview

import matplotlib.pyplot as plt
import two_column_text_read_00 as tctr
import plot_data_with_fit_00
import lowest_eigenvectors_00 as le
import univariate_statistics_00 as us
import fit_curve_array_00
import quadratic_fit_00 as qf
import equations_of_state as eos
import statistics as st
import numpy as np
import generate_matrix as gm

filename = 'Ge.Fd-3m.GGA-PBEsol.volumes_energies.dat'
display_Graph = True
display_graph2 = True
my_eos = 'birch-murnaghan'
potential_name = 'square'
number_of_dimensions = 100
potential_parameter = 200
minimum_x = 1  # Number I chose
maximum_x = 400  # Number I chose


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

# 7. Define a function to covert received data from 6. from atomic units to cubic bohr/atom, rydberg/atom, and rydberg/cubic bohr X
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
# You should use raw strings (precede the quotes with an 'r'), and surround the math text with dollar signs ($) X
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
    x_CS = x_min + 0.05 * x_range  # Coordinates of x for chemical symbol
    y_CS = y_max - 0.05 * y_range  # Coordinates of y for chemical symbol
    x_CSS = x_min + x_range/2  # Coordinates of x for CSS
    y_CSS = y_max - y_range/2  # Coordinates of y for CSS
    x_K = x_min + x_range/2  # Coordinates of x for bulk modulus
    y_K = ((y_max - y_range/2) + 0.0005)  # Coordinates of y for bulk modulus
    x_EqV = (x_min + x_range/2)
    y_EqV = ((y_max - y_range/2) - 0.004)
    print(AA)
    plt.title('Birch Murnaghan Equation of State for Ge in DFT GGA_PBEsol', y=1.05) # Move title up so no overlapping
    plt.text(x_CS, y_CS, CS)
    print(CSS)
    plt.text(x_CSS, y_CSS, r' $ \ Fd}$3$m} $')  # Had to do it this way for italics
    print(bulk_modulus)
    plt.text(x_K, y_K, r' $K_0$ =0.00456392914 GPa')  # Might need to change this with 'birch-murnaghan'
    plt.axvline(x=155.59, ymin=-0.1, ymax=-0.0905, ls='--', color='black')
    print(equilibrium_volume)  # Found value, put value in
    plt.text(x_EqV, y_EqV, r' $V_0 = 155.59 \AA^3/atom $')
    plt.figtext(0, 0, 'Created By Rhett Kliger 2020-5-14')

    #return


annotate_graph(CS, CSS, AA, bulk_modulus, equilibrium_volume, x_min, x_max, y_min, y_max)

if display_Graph == True: # Test if True
    plt.show(display_Graph)  # Show
elif display_Graph == False:  # Basically otherwise
    plt.savefig('Kliger_Rhett_Ge.Fd-3m.GGA-PBEsol.png')

# 10. Display graph True, is at top of script X

# Visualize Vectors In Space

# 1. Generate the matrix according to the parameters with the generate_matrix function X
square_matrix = gm.generate_matrix(minimum_x, maximum_x, number_of_dimensions, potential_name, potential_parameter)
print('Matrix Generated with Given Values: ')
print(square_matrix)

# 2. Use your lowest_eigenvectors function to calculate and
# return the three eigenvectors and eigenvalues of the matrix requested on the Final Exam Data page. X
eigenvalues, eigenvectors = le.lowest_eigenvectors(square_matrix, number_of_eigenvectors=3)
print("Here are the eigenvalues and eigenvectors: ")
print(eigenvalues, eigenvectors)

# 3. Use NumPy's linspace to generate the grid of spatial points between -10 and 10 with Ndim points X
# N dim = 100 is listed as number_of_dimensions
# numpy linspace(start, stop, number of points)
grid_of_spatial_points = np.linspace(-10, 10, number_of_dimensions)
print('This is the Grid of Spatial Points: ')
print(grid_of_spatial_points)

# 4. Plot the eigenvectors against the grid with a solid contrasting color curves:
# If the lowest eigenvalue eigenvector is in your set, you should make the eigenvector positive if the components are negative.

plot1 = plt.plot(grid_of_spatial_points, eigenvectors[0][0:number_of_dimensions], color='blue')
plot2 = plt.plot(grid_of_spatial_points, eigenvectors[1][0:number_of_dimensions], color='red')
plot3 = plt.plot(grid_of_spatial_points, eigenvectors[2][0:number_of_dimensions], color='green')
plt.xlabel('x [a.u.]')  # a.u. is atomic units
plt.ylabel(r' $\psi_n$(x)[a.u.]')
plt.legend((plot1, plot2, plot3),(r'$\psi_n$,$E_1$=(1)[a.u.]', r'$\psi_n$,$E_2$=(2)[a.u.]', r'$\psi_n$,$E_3$=(3)[a.u.]'))
plt.axis([-10, 10, max(eigenvectors[0]) - 2, max(eigenvectors[0]) + 2])  # Set vertical axis 2X max eigenvector component

# 5. Plot black horizontal line at psi = 0
# I can use axhline which is for horizontal lines
plt.axhline(color="black")

# 6. Sign the graph "Created by 2020-05-12" in the bottom left of the plot below the axes labels and tickmarks.
plt.text(-9, -1.5, 'Created By Rhett Kliger 2020-05-14')

# 7. Title the graph
plt.title('Select Wavefunctions for a Square Potential on a Spatial Grid of 100 Points')

# 8. Make a display graph variable
if display_graph2 == True: # Test if True
    plt.show(display_graph2)  # Show
elif display_graph2 == False:  # Basically otherwise
    plt.savefig('Kliger_Rhett_Wavefunctions_Square_Potential.png')
