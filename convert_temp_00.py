#Rhett Kliger
# convert_temp_00.py

def C2F(C):  # Celsius to Fahrenheit
    F = 9/5 * C + 32
    return F


def F2C(F):  # Fahrenheit to Celsius
    C = 5/9 * (F - 32)
    return C


def C2K(C):  # Celsius to Kelvin
    K = C + 273.15
    return K


def K2C(K):  #Kelvin to Celsius
    C = K - 273.15
    return C

def F2K(F):  # Fahrenheit to Kelvin
    K = F2C(F) + 273.15
    return K


def K2F(K): # Kelvin to fahrenheit
    F = (C2F(K) - 273.15)
    return F
if __name__ == '__main__':
    K = 0
    print('Absolute zero = %g K, %g C, %g F' % (K, K2C(K), K2F(K)))
    C = 0
    print('Freezing point of water = %g K, %g C, %g F' % (C2K(C), C, C2F(C)))
    F = 0
    print('Freezing point of brine = %g K, %g C, %g F' % (F2K(F), F2C(F), F))
