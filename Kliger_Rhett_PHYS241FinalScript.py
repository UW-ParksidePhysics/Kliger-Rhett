#Final Script
#Rhett Kliger

# Overview
import matplotlib.pyplot as plt
import two_column_text_read_00
import plot_data_with_fit_00
import lowest_eigenvectors_00
import univariate_statistics_00, statistics
import fit_curve_array_00
import quadratic_fit_00
import equations_of_state
# So from 1 on parse
filename = 'Ge.Fd-3m.GGA-PBEsol.volumes_energies.dat'

# I tried to do the overview here so is it ok to remove this portion?
data = two_column_text_read_00.two_column_text_read(filename)  #Reads the file of two column data or should
print(data)
exit()

#plot_data_with_fit_00.plot_data_with_fit(data, fit_curve=2, data_format=0, fit_format=0)

#lowest_eigenvectors_00.square_matrix()

#lowest_eigenvectors_00.lowest_eigenvectors(square_matrix=10, number_of_eigenvectors=3)
#print(lowest_eigenvectors_00.lowest_eigenvectors)


# Fit an Equation of a State
def parse_file_name(filename):
    print("Ge.Fd-3m.GGA-PBEsol")  # Return from filename
    two_column_text_read_00.two_column_text_read(filename)
    print(two_column_text_read_00.two_column_text_read(filename)) #Data from the file
    univariate_statistics_00.univariate_statistics(data) # Take the data from the file and pull out statistics
    fit_curve_array_00.fit_curve_array(statistics)
    equations_of_state.fit_eos(quadratic_coefficients=3)

# Bohr is unit of length, Rydberg is unit of energy,
# First column is volumes, second column is energies
def convert_units(data):
    return data[0]/data[1]  # Data 0 is volumes, data 1 is energies




