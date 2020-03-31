#3.23 Heaviside Function
def Heaviside(x): # Here I define the Heaviside function based off of the parameters I've been given
    if x < 0:
        return 0
    elif x >= 0:
        return 1
print(Heaviside(-10)) # When x is 10 it should print out 0
print(Heaviside(-10**-15)) #When x is negative value is less than 0 so should output 0
print(Heaviside(10**-15)) #When x is 10^-15 it should be larger than zero and output 1
print(Heaviside(10)) # When x is 10 it is larger than 0 and should output 1

#OVERALL OUTCOME: SUCCESS