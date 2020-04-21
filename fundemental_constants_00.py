# Make a function that reads and interprets the text in the file, and there after returns the dictionary.


def read_constants(filename):
    infile = open(filename, 'r')
    constants = {}
    infile.readline()
    infile.readline()
    for line in infile:
        name_of_constant = ' '.join(line.split()[:-2]) # Forgive me if you already said this but why -2, value of constant is second from the right. : end at that point

        value = (line.split()[-2])

        constants[name_of_constant] = value  # Constants is dictionary, name of constant is the keyword, the value is what we are looking for Sorry i didn't hear that

    infile.close()

    return constants


constants = read_constants('constants_00.py')
print('--------------------------------')
print(constants)
print('--------------------------------')