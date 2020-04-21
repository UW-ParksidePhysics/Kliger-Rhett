# Make a function that reads and interprets the text in the file, and there after returns the dictionary.


def read_constants('constants_00.py'):
    infile = open('constants_00.py', 'r')
    constants = {}
    for line in infile:
        words = line.split()
        value = float(words(-1))
    infile.close()
    return constants
print('--------------------------------')
print(constants, value)
print('--------------------------------')